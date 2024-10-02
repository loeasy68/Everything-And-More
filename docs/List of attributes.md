# List of attributes
When in json, These attributes have a key-value pair one of the options will be ability and that just points to the file that handles that abitily

Fatness(-2 Speed, +2 Hunger Bar)
Dubious(1 Minute Nausea, 2 Minute random buff/debuff)
Gills(Permanent Water Breathing, Slower on land)
Decomposition(Eat Anything Organic)
Omnivore(Eat anything*)
Glass Canon(-2 Hearts, +2 Strength)
Bulk(+2 Health, +2 Hunger Bar, -1 Speed)
Navigator(Save a location permanently)
Smart(+10% Research speed)
Hollow Bones(+2 Speed, +2 Jump, -2 Hearts, -2 Strength)
Thick Skin(+3 Hearts, +1 Hunger Bar, +1 Defense)
Weak Speedster(-5 Hearts, +3 Speed, +3 Jump, +1 Strength)
Buff Speedster(+1 Heart, +2 Speed, +3 Jump, +2 Strength)
THE EATER(+5 Hunger Bar, -3 Speed)
Le chonk(+6 Hunger Bar, +2 Heath, -5 Speed)
Slow Speedster(+3 Hunger Bar, +1 Speed, +2 Health)
Warrior(+4 Strength, +3 Health)
    Quick(+3 Strength, +3 Speed, -2 Health)
    Weak(+5 Strength, -2 Health)
    Fragile(+5 Strength -5 Health)
Attacker(+2 Strength)
Weird(-2 Hunger, Permanent nausea)
Hardness(+3 Defense)
Photosynthesis(Slowing Regain Hunger During The Day)
Plant Clone(Create a plant that slowly grows that you can posses after death. Lose all genetics and gain photosynthesis after reincarnation. Stats may vary depending on how grown the clone was.)
Degrade(Be able to nibble on tools for extra hunger)
Eating+(Gain more hunger from eating)
Plastic Eating(Be able to eat plastic)

# List of possible attribute IDs

**S** - Speed
**H** - Health
**A** - Attack/Strength
**U** - Hunger Bar
**D** - Defense
**N** - Blank(Put value of minutes in json) Minute Nausea
**2R** - 2 minutes of random buff/debuff of strength
**V** - Vanishing(Makes the dna vanish)
**PWB** - Peramant Water breathing(1 means true)
**SWL** - Slowness on land
**EAO** - Eat anything organic(1 means true)
**EA** - Eat anything(1 means true)
**RS** - Reasearch Speed
**J** - Jump Boost

All others will be listed with their mc effect IDs

# How abilities work

Special abilities will be handled by a seperate script

# Json DNA structure
```json
{
    "Boost": {"Attribute ID": "Attribute Strength"},
    "Ability": "Ability Handler.java"
}
```
Example for thick skin
```json
{
    "Boost": {
        "H": 3,
        "U": 1,
        "D": 1},
    "Ability": "Empty"
}
```