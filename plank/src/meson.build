plank_theme_dir = plank_default_theme_dir

variants = [
  'default',
  'dark',
]

foreach accent: enabled_accent_colors
  if enabled_accent_colors.contains(accent)
    variants += (get_option('default') ? [accent] : [])
    variants += (get_option('dark') ? [ accent + '-dark' ] : [])
  endif
endforeach

foreach variant: variants
  if not get_option('cinnamon-shell')
    warning('cinnamon-shell is not enabled, so we won\'t be able to generate plank themes.')
    continue
  endif
  
  is_dark = variant == 'dark' or variant.endswith('-dark')
  is_variant = variant != 'default'
  variant_base_name = is_dark ? variant.split('-dark')[0] : variant
  variant_suffix = is_variant ? '-@0@'.format(variant)  : ''
  theme_full_name = meson.project_name() + variant_suffix
  is_custom_accent = enabled_accent_colors.contains(variant_base_name)
  message(theme_full_name)

  install_dir = join_paths(plank_theme_dir, theme_full_name)
  target_name = theme_full_name + '-' + 'dock.theme'
  message(target_name)

  colors_definitions = sucharu_colors_defs['@0@'.format(theme_full_name)]
  accented_theme = custom_target(
    '___'.join('@0@'.format(target_name).split('/')),
    input: 'dock.theme.in',
    output: target_name,
    command: [
      colorize_dummy_svg,
      colors_definitions,
      '--input-file', '@INPUT@',
      '--output-folder', '@OUTDIR@',
      '--variant', variant,
      '--hex2rgb', 'True',
    ],
    depends: colors_definitions,
    build_by_default: true,
  )
  # rename theme variant
  replacestring = theme_full_name.replace(meson.project_name(), '') + '.svg'
  curr_theme = join_paths(meson.current_build_dir(), ('dock.theme' + replacestring))
  # install_data(curr_theme,
  #   rename: 'dock.theme',
  #   install_dir: install_dir)

  meson.add_install_script('rename-plank-theme.sh', curr_theme, install_dir)
endforeach
