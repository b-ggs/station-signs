# Rochor · 梧槽 · ரோச்சோர்

![Rochor station name sign](rochor.png)

Singapore. Station **DT13** on the MRT Downtown Line, between Little India (DT12) and
Bugis (DT14).

Visited in June 2026 with David and Arjan.

Built in VectorCraft by **Claude Opus 5.5**.

This is the platform's station name sign: the DT 13 code badge, the name in English, Chinese
and Tamil, and the Downtown Line's blue bar along the bottom. English and the code use
[IdentityFont](https://github.com/jglim/IdentityFont), an open reconstruction of LTA's
LTAIdentity. The source is [`rochor.vectorcraft`](rochor.vectorcraft); see
[`AGENTS.md`](AGENTS.md) for design notes.

## Export

Run from this folder:

```sh
mkdir -p exports
vectorcraft-cli convert rochor.vectorcraft exports/rochor.pdf
```
