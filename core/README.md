# `ff8000`

A customizable, modular, fully-typed discord bot written in python (hikari). Designed for a mix of standard modules as well as easy integration with your own custom functionality, all in one sleek bot user on your server.

Forked from one of my projects, ProtoBan.

## Todo

- Add `pre-commit` with hooks:
  - `ty`
  - `ruff`
- Fix shellcheck errors in `run.sh`
- Add `CONTRIBUTING.md`, with among other guidelines:
  - require AI disclosure if used
- Tweak the documentation on how to use `run.sh`'s modes (`dev`, `prod`), and suggest `./run.sh prod` instead of not putting an argument (which defaults to `dev` which might result in dev features being enabled.)
- Add an example mod(s) and include the suggested dir/file structure (e.g. `mkdir -p commands/admin events hooks view`) as well as the required __init__.py shape.
- Add a documentation page (maybe use Github Wiki?) with a guide on how to make your own mod
  - Perhaps the following four inside some `ModInitResult` struct
  - How should a mod declare its privilidged intents? (in its readme?)
  - How should a mod declare its required bot install modes (user install, guild install)
  - How should a mod declare its required role permissions
  - How should a mod declare its bot emojis
    - Possibly `_.emoji` - standard config and resolution? Maybe just tools to parse a """ """ string
    - How should the emoji IDs be put into the static config?
- Implement the stdlib mod (`mods._`)
  - Database (`sqlmodel`)
  - Settings (config)
  - Localization
  - Prefix commands (shell-like parsing with forked fixed version of arguably or a new written one, name it nya-cli)
  - ...
- ~~Use uv workspaces and git submodules for the mods to be able to define their own dependencies. ~~
  - Alternative: use namespace package: `ff8000.mods` and have ~~pip~~ *uv* handle the order resolution.
- Everytihng in the google keep note
- Update the license so it correctly works with the mods (AGPL currently doesnt let anyone have private mods, which is not what i wnat, but i do want AGPL for the bot's core)

Bot like RedDiscordBot (with module system and stdlib), but with arguably-like command parsing (arguably has some bugs, just make your own command parsing lib like nya-cli and have it be able to hook into any list[str] instead of being tied to sys.argv, for interpolations use nya-execute or whatever it's called
use absolute import paths so import shit doesn't get fucked. mods can depend on other mods. pick mod execution order like the other version of modular bot - dependencies come first. base ("_") mod always comes first.

‼️ EVEN BETTER: mods are submodules, a namespace package architecture is used where `botname.mods` is a namespace package (no __init__.py), mods declare their own dependencies via uv workspaces:
[tool.uv.workspace]
members = ["mods/*"] ;; PACKAGE NAME IDEAS (later choose one): "ff8000", "bottom" ‼️for db use sqlmodel, see example here https://pastebin.com/dUXDGYXg with alembic for migraitons

## Installation & Usage

1. Install source code via git: `git clone <repo url>`, **definitely fork this repository** to make changes like: adding your own mods, configuring static config files of said mods.

2. Install `uv` python package manager (through your distro's package manager
   or `pipx` or [Astral's (uv's authors) script][uv-docs], (descending order of
   recommendation))

3. Use the `run.sh` script.

> `./run.sh`

by default `dev` environment is used

> [!WARNING]
> `- Testmode` markers and a few developer-oriented features (which probably
> shouldn't be visible to a user) will be enabled in dev mode, for production
> use `prod` mode
>
> **`./run.sh prod`**

select environment with the first positional argument

> `./run.sh dev --version`

any further arguments are passed to the script (note that due to how the `run.sh`
script works, you have to supply at least ANYTHING as the environment (first
positonal argument) to be able to pass arguments to the cli script handler
(e.g. `--help`, `--version`, etc.))

Note that the above require the use of `pass` password manager with the bot
token at the following path, If you wish to override the token (with your own
password manager's cli/a file on disk/pasted from clipboard), use
the following env variable: `OVERRIDE_TOKEN="your_token"`
(e.g. `OVERRIDE_TOKEN=... ./run.sh prod`)

[uv-docs]: https://docs.astral.sh/uv/getting-started/installation/
