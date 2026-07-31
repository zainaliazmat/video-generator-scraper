# Finance-video scaffold

Copy this whole directory to start a new cut (`fin-build` step 1). It holds the
binaries every finance composition vendors and which the vault archive
deliberately drops as regenerable-but-not-actually-regenerable:

| File | Why it's here |
|---|---|
| `package.json` + `package-lock.json` | pins the hyperframes version — `npm i -D`, never bare `npx --yes` |
| `assets/js/gsap.min.js` | vendored; **no CDN reference of any kind** in a composition |
| `assets/js/lottie.min.js` | vendored lottie-web 5.12.2 — load it BEFORE `motion.js`, and only in a cut that actually uses a Lottie |
| `assets/fonts/NotoSansFinance-var.woff2` | self-hosted FinanceSans |
| `assets/img/grain.png` | the grain overlay texture |

It exists so scaffolding never depends on a sibling video surviving: a shipped
video is deleted from `studio/` (finished-video rule, `vault/CLAUDE.md`). The
*composition* reference is the newest archived
`vault/videos/<slug>/src/{hi,en}/index.html`; this dir is only the binaries.
