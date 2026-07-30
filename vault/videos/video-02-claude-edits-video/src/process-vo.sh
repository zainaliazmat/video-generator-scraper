#!/bin/bash
# Studio VO chain (order per broadcast practice: HPF -> denoise -> comp ->
# de-ess -> EQ), then two-pass linear loudnorm to -16 LUFS / -1.5 dBTP,
# then 40ms/120ms edge fades to kill the hard-cut click.
set -e
SRC="$1"; OUT="$2"
CHAIN="highpass=f=80:poles=2,afftdn=nr=10:nf=-42,\
acompressor=threshold=-20dB:ratio=3:attack=10:release=150:makeup=3,\
deesser=i=0.4,\
equalizer=f=250:t=q:w=1.4:g=-2,equalizer=f=3800:t=q:w=1.2:g=2,\
equalizer=f=10500:t=q:w=1.5:g=1.5"

# pass 1: measure
M=$(ffmpeg -hide_banner -i "$SRC" -af "$CHAIN,loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p')
mi=$(echo "$M" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['input_i'],d['input_tp'],d['input_lra'],d['input_thresh'],d['target_offset'])")
read -r I TP LRA TH OFF <<< "$mi"

# pass 2: linear gain + fades (areverse anchors the fade-out to the true end)
ffmpeg -hide_banner -loglevel error -y -i "$SRC" \
  -af "$CHAIN,loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=$I:measured_TP=$TP:measured_LRA=$LRA:measured_thresh=$TH:offset=$OFF:linear=true,aresample=48000,afade=t=in:st=0:d=0.04,areverse,afade=t=in:st=0:d=0.12,areverse" \
  -ac 1 -ar 48000 -c:a pcm_s16le "$OUT"
