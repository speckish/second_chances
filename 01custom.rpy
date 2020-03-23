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
            glog(name)
            renpy.image(name, im.FactorScale(file, z, bilinear=img_config['bilinear']))
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

    renpy.register_statement("yuki", parse=parse_yuki, execute=execute_yuki, lint=lint_yuki)
