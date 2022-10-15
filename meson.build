project('Sucharu',
        version: '2.0.5',
        meson_version: '>= 0.60',
        license : ['GPL3', 'CC BY-SA 4.0'],
        default_options: ['prefix=/usr'])

fs = import('fs')
gnome = import('gnome')

python = find_program('python3')
sassc = find_program('sassc')

subdir('common')

components = [
  'metacity',
  'gnome-shell',
  'gtk',
  'gtksourceview',
  # 'sounds',
  # 'sessions',
  # 'ubuntu-unity',
  'xfwm4',
  'cinnamon-shell',
]

enabled_accent_colors = get_option('accent-colors')

foreach component: components
  if not get_option(component)
    message('Skipping component ' + component)
    continue
  endif

  message('\n\n\tBuilding component ' + component)
  subdir(component)

endforeach

run_command('make', check: true)
