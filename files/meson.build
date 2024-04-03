# install accent to /usr/share/cinnamon/styles.d
cinnamon_accents_dir = join_paths(get_option('datadir'), 'cinnamon/styles.d')

accent_style_asset_dir = meson.current_source_dir() + '/accents'
accent_style_assets = files(
  run_command(
    'find', accent_style_asset_dir, '-name', '*.styles', check: true
  ).stdout().strip().split('\n')
)

# install accent style assets
foreach accent_style_asset: accent_style_assets
	install_data(accent_style_asset, install_dir: cinnamon_accents_dir)
endforeach
