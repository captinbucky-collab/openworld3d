# CHISHTI BRO: PAKISTAN OPEN WORLD — FINAL EDITION

A modular, playable GTA-style browser game prototype set in a fictional modern Pakistani city.

## Features
- Procedural city with 60+ buildings, roads, sidewalks, traffic lights and parks
- Third-person walking, sprinting, jumping, crouching and melee
- 12 drivable/traffic vehicles with fuel and damage values
- 36 roaming pedestrians and wanted-level police response
- Enterable buildings with generated multi-room interiors, furniture and stairs
- House purchase and owned-property save points, wardrobe and weapon locker
- Pistol, AK-47, shotgun and sniper slots; pickups, reload, firing and dropping
- Cash, health, stamina, inventory, minimap, shop and job rewards
- Day/night cycle and weather toggle
- Python launcher and GitHub Actions Windows EXE workflow
- GLTF/GLB loader integration with procedural fallback assets

## Run
Install Python 3.10+, then run `python launcher.py`. The browser opens automatically. Internet is required for Three.js CDN modules.

## Controls
WASD move/drive · Mouse look · Shift sprint · Space jump/handbrake · C crouch · Q punch · F enter/exit · E interact · B buy · 1–4 weapon · Left mouse shoot · R reload · G drop · M map · Tab inventory · Esc pause.

## Windows EXE
Push the project to GitHub. The workflow `.github/workflows/build-windows.yml` builds a Windows launcher. Download `CHISHTI-BRO-Windows-EXE` from the Actions artifact list. The EXE serves the game locally and opens it in a browser; it is not a native 3D engine executable.

## GLTF assets
`game/js/assets.js` contains a GLTFLoader registry. Add licensed `.glb`/`.gltf` models under `game/assets/models/` and register paths to replace procedural fallbacks. No copyrighted GTA assets are bundled.

## Scope
This is a feature-rich procedural prototype, not a commercial GTA V-scale production. Photorealistic art, advanced vehicle simulation, custom animation, voice acting and production-grade interiors need dedicated licensed assets and further development.
