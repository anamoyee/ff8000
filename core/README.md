# `ff8000`

A customizable, modular, fully-typed discord bot written in python (hikari). Designed for a mix of standard modules as well as easy integration with your own custom functionality, all in one sleek bot user on your server. Inspired by [Red-DiscordBot](https://github.com/cog-creators/red-discordbot)

Forked from one of my projects, ProtoBan.

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
