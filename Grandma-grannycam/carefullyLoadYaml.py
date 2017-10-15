
import yaml


def carefullyLoadYaml(f, p = ''):
    try:
        Yaml = yaml.load(open(p+f))
        return(Yaml)
    except Exception as e:
        print("failed to read yml Exeption:"+str(e))
        #raise Exception

