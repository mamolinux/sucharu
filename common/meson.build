colorize_dummy_svg = find_program('colorize-dummy-svg.py')
accent_colors_definitions_scss = join_paths(meson.project_source_root(), fs.parent(files('accent-colors.scss.in')[0]), fs.name(files('accent-colors.scss.in')[0]))
sucharu_colors_defs_scss = join_paths(meson.project_source_root(), fs.parent(files('sucharu-colors-defs.scss')[0]), fs.name(files('sucharu-colors-defs.scss')[0]))

sass_utils_scss = files([
    'sass-utils.scss',
])

test('sass-utils',
    sassc,
    args: [
        files('test-sass-utils.scss'),
        '/dev/null',
    ])
