# Licence clearance: rebuild code pack (skeleton)

Checked 4 Oct 2026 against each repo's LICENSE file (raw GitHub) or the vendor's licence page. This is an engineering read, not legal advice. Re-check the licence file in the exact repo and version the fleet copies from.

## Summary

| Source | Licence (verified) | Copy into a site/app? | Attribution needed |
|---|---|---|---|
| anime.js | MIT, (c) 2025 Julian Garnier | Yes | Keep licence + copyright notice |
| three.js | MIT, (c) 2010-2026 three.js authors | Yes | Keep licence + copyright notice |
| GSAP (core + all plugins) | GSAP Standard License (Webflow), effective 30 Apr 2025. Not MIT | Use yes, as a dependency. Do not re-host as a bundle | Do not remove GSAP notices/branding |
| Magic UI (free, open repo) | MIT, (c) Magic UI | Yes | Keep licence + copyright notice |
| Magic UI Pro (paid templates/blocks) | Proprietary purchaser licence | Only if purchased, never redistribute | n/a - flag |
| React Bits | MIT + Commons Clause, (c) 2026 David Haz | Yes, as part of an app/site only | Keep copyright notice |
| liquid-glass-react (rdev) | MIT, (c) 2025 Max Rovensky | Yes | Keep licence + copyright notice |
| tailwindcss-claymorphism (dulltackle) | MIT, (c) 2022 dulltackle | Yes | Keep licence + copyright notice |
| clay.css (codeAdrian) | NOT VERIFIED - LICENSE file did not load, README showed no licence line | Do not copy until confirmed | Unknown |
| Other "liquid glass" repos (simple-liquid-glass, glass-refraction, samasante, kucukkanat, dpawlikowski) | NOT CHECKED | Do not copy until each is checked | Unknown |

## Per-source rules

**anime.js** - https://raw.githubusercontent.com/juliangarnier/anime/master/LICENSE.md
MIT. Copy, modify, bundle freely, commercial included. Keep "Copyright (c) 2025 Julian Garnier" and the MIT text in a THIRD_PARTY_LICENSES file or the bundle banner.

**three.js** - https://raw.githubusercontent.com/mrdoob/three.js/dev/LICENSE
MIT. Same rule. Note: examples, shaders and models in the repo can carry their own licences or separate authors. Check headers on any file copied from /examples, and do not assume bundled textures/models are MIT.

**GSAP** - https://gsap.com/community/standard-license/ (the GSAP repo's own licence section points to this)
Custom licence, not open source. Now free for commercial use including former Club plugins (SplitText, MorphSVG etc.). Allowed: use in any site or web app. Not allowed: building a no-code visual animation builder that competes with Webflow, reverse engineering to make a competitor, removing proprietary notices. Webflow can revoke for breach and amend terms. Safe route: install from npm and import; do not paste GSAP source into the code pack or republish it. AI-generated GSAP code is explicitly fine. Flag: if the pack is ever sold or shared as a template builder, re-read the Prohibited Uses clause.

**Magic UI (free)** - https://raw.githubusercontent.com/magicuidesign/magicui/main/LICENSE.md
MIT. Copy components freely; keep copyright line in the file or licence list.
**Magic UI Pro** - https://pro.magicui.design/license
Not safely reusable unless P has bought it. Even then: no redistribution or sharing, even modified; no claiming authorship; no competing templates. Fleet must not copy anything from pro.magicui.design. Only use components from the open magicui repo.

**React Bits** - https://raw.githubusercontent.com/DavidHDev/react-bits/main/LICENSE.md
MIT + Commons Clause. Free for personal and commercial use as part of an application, website or product. Not allowed: selling, sublicensing or redistributing the components themselves, alone, in a bundle or as a port. Flag: a downloadable "code pack" containing React Bits files is a redistribution risk. Keep React Bits files inside the built site only, or have the pack reference the npm/CLI install instead of shipping the source. Commons Clause is not an OSI open-source licence.

**liquid-glass-react** - https://raw.githubusercontent.com/rdev/liquid-glass-react/master/LICENSE
MIT (licence text has no "MIT" title, but the grant is the standard MIT wording). Keep "Copyright 2025 MAX ROVENSKY". It is one candidate among several liquid glass repos; pick this one by default.

**Claymorphism**
- tailwindcss-claymorphism: https://raw.githubusercontent.com/dulltackle/tailwindcss-claymorphism/main/LICENSE - MIT, keep notice.
- clay.css (https://github.com/codeAdrian/clay.css/): licence unconfirmed. Treat as all rights reserved until someone reads its LICENSE in the repo or npm metadata. Writing your own claymorphism shadows in plain CSS is always safe (the style is not protected, only the code).

## Rules for the fleet

1. Only copy code from a repo whose LICENSE is listed MIT above. Record repo URL + commit + licence for every copied file.
2. Add a THIRD_PARTY_LICENSES.md to the build with every copyright line and MIT text used.
3. Prefer npm install over pasting source for GSAP, three.js, anime.js.
4. No code from paid or "pro" sites, Codepen/Dribbble snippets, or Awwwards/Apple/Ghibli sites. CodePen defaults to MIT only if the pen says so; check each.
5. Images, fonts, video and 3D models are separate from code licences. Check each (earlier portfolio rounds already have an asset manifest). Studio Ghibli artwork or Apple assets are not reusable; "Ghibli style" is fine, copied frames are not.
6. Do not ship the pack as a downloadable/resold bundle without re-checking GSAP and React Bits terms.

## Open items
- Confirm clay.css licence.
- Check any other liquid glass repo before use.
- Check licences for any further sources the fleet adds (e.g. Aceternity UI, shadcn/ui, Motion) - not covered here.
