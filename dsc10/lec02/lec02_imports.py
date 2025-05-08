from IPython.display import IFrame
def show_nested_eval():
    src = 'https://docs.google.com/presentation/d/e/2PACX-1vQpW0NzwT3LjZsIIDAgtSMRM1cl41Gp_Lf8k9GT-gm5sGAIynw4rsgiEFbIybClD6QtxarKaVKLbR9U/embed?start=false&loop=false&delayms=60000&rm=minimal" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"'
    width = 960
    height = 569
    return IFrame(src, width, height)