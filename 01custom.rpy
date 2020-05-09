init -1 python:
    z = 1.0
    img_config = {'bilinear': False,
                  'folders': {
                      'characters': {'trimmed': True,
                                     'separator' : '_'},
                      'bg': {}
                  }}

    for file in renpy.list_files():
        if file.startswith('images/') and (file.endswith('.png') or file.endswith('.jpg')):
            folder = file.split('/')[1]
            conf = img_config['folders'].get(folder, {})
            separator = conf.get('separator',' ')
            name = file.replace('images/','').replace('/', separator).replace('.png','').replace('.jpg','').strip(separator)
            if conf.get('trimmed', False):
                name = name.replace(folder, '').strip(separator)
            renpy.image(name, im.FactorScale(file, z, bilinear=img_config['bilinear']))
            renpy.image(separator.join([name, 'flip']), im.Flip(im.FactorScale(file, z, bilinear=img_config['bilinear']), horizontal=True))
            if "neutral" in name:
                name = name.replace('neutral','').strip(separator)
                renpy.image(name, im.FactorScale(file, z, bilinear=False))

python early:
    def parse_yuki(lex):
        what = lex.rest()
        if what == "None":
            return None
        else:
            return "yuki " + what

    def execute_yuki(what):
        setattr(renpy.store, "yuki_side_image", what)

    def lint_yuki(o):
        pass

    def parse_aurelia(lex):
        what = lex.rest()
        if what == "None":
            return None
        else:
            return "cat " + what

    def execute_aurelia(what):
        setattr(renpy.store, "aurelia_side_image", what)

    def lint_aurelia(o):
        pass

    def parse_q(lex):
        what = lex.rest()
        if what == "None":
            return None
        else:
            return "quinn " + what

    def execute_q(what):
        setattr(renpy.store, "quinn_side_image", what)

    def lint_q(o):
        pass


    renpy.register_statement("yuki", parse=parse_yuki, execute=execute_yuki, lint=lint_yuki)
    renpy.register_statement("aurelia", parse=parse_aurelia, execute=execute_aurelia, lint=lint_aurelia)
    renpy.register_statement("qu", parse=parse_q, execute=execute_q, lint=lint_q)
