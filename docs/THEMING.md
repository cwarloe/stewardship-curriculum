# Theming: one file sets the look

**Default:** every color and font on the web pages in `docs/` comes from `docs/tokens.css`. Pages use
`var(--name)`, not a raw value such as `#1f5f9e` or `Arial`. Change a value in `tokens.css` and every page
follows. `scripts/check_theme.py` checks this in CI.

- **Names say what the color is for**: `--accent`, `--paper`, `--ink`, `--line`. Not `--blue`.
- **Palettes are attributes.** `bbp-outline.html` switches with `<body data-theme="blue|green|orange|purple|gray">`.
  Each palette block in `tokens.css` lists only what differs from blue.
- **Text on a color has its partner**: text on `--accent` uses `--on-accent`; text on the tints uses `--accent-ink`.
- **Exceptions**: a line that has to keep a raw value says why in a comment containing `theme-ok: <reason>`.
  The checker skips it.

| To | Do |
|---|---|
| Recolor a palette | Edit its block in `docs/tokens.css` |
| Add a palette | Add a `[data-theme="name"]` block with the values that differ |
| Need a new kind of color | Add a name that says its job to `docs/tokens.css`, then use it |

Run `python3 scripts/check_theme.py` before pushing a change to a page.
