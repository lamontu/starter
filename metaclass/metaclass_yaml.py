import yaml

class Monster(yaml.YAMLObject):
  yaml_tag = '!Monster1'
  def __init__(self, name, hp, ac, attacks):
    self.name = name
    self.hp = hp
    self.ac = ac
    self.attacks = attacks
  def __repr__(self):
    return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
       self.__class__.__name__, self.name, self.hp, self.ac,
       self.attacks)

yaml.load("""
--- !Monster1
name: Cave spider
hp: [2,6]    # 2d6
ac: 16
attacks: [BITE, HURT]
""", Loader=yaml.Loader)

Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT'])

print(yaml.dump(Monster(
    name='Cave lizard', hp=[3,6], ac=16, attacks=['BITE','HURT'])))

