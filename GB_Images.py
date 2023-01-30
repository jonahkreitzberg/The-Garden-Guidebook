import sys
sys.path.insert(1, '../LocalBoulders')
from dataStructure import Photo, Topo, AreaMap, SubAreaMap
from GB_Book import book
#from Area_Main import *
#from Area_PinkTag import *
#from Area_Cliffs import *
#from Area_Upper import *
#from Area_Quartz import *


# Photo(name='Austin Powers',
#       fileName='AustinPowers.jpg',
#       parent=book.formations['Mini Me'],
#       route=book.routes['austinPowers'],
#       credit='Andrew Child',
#       description='Carson cranking across the face on Austin Powers.'),
Photo(name='Riptide',
      fileName='Riptide.jpg',
      parent=book.formations['Undertow'],
      route=book.routes['Riptide'],
      credit='Andrew Child',
      description='Rob on Riptide')
Photo(name='Fight Club',
      fileName='FightClub2.jpg',
      parent=book.formations['Fight Club'],
      route=book.routes['Fight Club'],
      credit='Andrew Child',
      description='Michael near the top of Fight Club.')
Photo(name='Octernal',
      fileName='Octurnal.jpg',
      parent=book.formations['Meth Lab Back Side'],
      route=book.routes['Octernal'],
      credit='Andrew Child',
      description='Carson landing the big throw on Octernal. Classic!')
# Photo(name='Smackdown',
      # fileName='Smackdown.jpg',
      # parent=book.formations['Meth Lab Back Side'],
      # route=book.routes['smackdown'],
      # credit='Carson Dension',
      # description='Andrew posting up at the start of Smackdown')
Photo(name='Ground up Blowie',
      fileName='blowie.jpg',
      parent=book.formations['Azain'],
      route=book.routes['Ground up Blowie'],
      credit='Michael Gardener Brown',
      description='Andrew strugling to finde a finger lock on Ground up Blowie')
Topo(name='Bitchin Corners',
     parent=book.formations['Bitchin Corners'],
     fileName='bitchin.svg',
     size='h',
     description='Bitchin Corners',
     routes={
         'path1002': book.routes['Bitchin Corners'],
         'path1029': book.routes['Bitchin Corners'],
         'path1014': book.variations['Bitchin Corners Sit'],
         'path1031': book.variations['Bitchin Corners Sit'],
     })
Topo(name='Baldo',
     parent=book.formations['Baldo'],
     fileName='baldo.svg',
     size='h',
     description='Baldo',
     routes={
         'path862': book.routes['Frontside Baldo'],
         'path864': book.routes['Frontside Baldo'],
     })
Topo(name='Overhand',
     parent=book.formations['Overhand'],
     fileName='overhand.svg',
     size='h',
     description='Overhand',
     routes={
         'path293': book.routes['Overhand'],
         'path443': book.routes['Overhand'],
     })
Topo(name='Hueco Wabo',
     parent=book.formations['Hueco Wabo'],
     fileName='hueco.svg',
     size='h',
     description='Hueco Wabo',
     routes={
         'path1918': book.routes['Hueco Wabo'],
         'path1920': book.routes['Hueco Wabo'],
     })
Topo(name='Azain Spire',
     parent=book.formations['Azain Spire'],
     fileName='azainSpire.svg',
     size='h',
     description='Azain Spire',
     routes={
         'path724': book.routes['Snakes and Martyrs'],
         'path726': book.routes['Snakes and Martyrs'],
     })
Topo(name='Three Star Ledge',
     parent=book.formations['Three Star Ledge'],
     fileName='3star.svg',
     size='h',
     description='Three Star Ledge',
     routes={
         'path300': book.routes['Three Star Ledge'],
         'path583': book.routes['Three Star Ledge'],
         'path514': book.variations['Three Star Ledge Variation'],
         'path529': book.variations['Three Star Ledge Variation'],
         'path585': book.variations['Three Star Ledge Variation'],
     })
Topo(name='The Good',
     parent=book.formations['The Good'],
     fileName='good.svg',
     size='f',
     description='The Good',
     routes={
         'path1453': book.routes['The Good'],
         'path1459': book.routes['The Good'],
         'path1451': book.routes['Another'],
         'path1457': book.routes['Another'],
         'path1445': book.routes['Next to the Good'],
         'path1447': book.routes['Next to the Good'],
         'path1449': book.routes['Next to the Good'],
         'path1455': book.routes['The Good Slab'],
         'path1461': book.routes['The Good Slab'],
     })
Topo(name='Fight Club Right Side',
     parent=book.formations['Fight Club'],
     fileName='fightClub.svg',
     size='h',
     description='Fight Club Right Side',
     routes={
         'path1145': book.routes['The Ear'],
         'path1151': book.routes['The Ear'],
         'path1143': book.routes['Fight Club'],
         'path1153': book.routes['Fight Club'],
         'path1147': book.routes['Vince'],
         'path1149': book.routes['Vince'],
     })
Topo(name='Fight Club Left Side',
     parent=book.formations['Fight Club'],
     fileName='fightClub2.svg',
     size='h',
     description='Fight Club Left Side',
     routes={
         'path1297': book.routes['Fight Club 2'],
         'path1303': book.routes['Fight Club 2'],
         'path1299': book.routes['Fight Club'],
         'path1301': book.routes['Fight Club'],
         'path1293': book.routes['Brewmaster'],
         'path1305': book.routes['Brewmaster'],
     })
Topo(name='E\'s Dirty B',
     parent=book.formations['E\'s Dirty B'],
     fileName='eDirty.svg',
     size='h',
     description='E\'s Dirty B',
     routes={
         'path1003': book.routes['E\'s Dirty B'],
         'path1005': book.routes['E\'s Dirty B'],
     })
Topo(name='Car Alarm Downhill Side',
     parent=book.formations['Car Alarm'],
     fileName='carAlarm.svg',
     size='f',
     description='Car Alarm Downhill Side',
     routes={
         'path674': book.routes['Car Alarm Traverse'],
         'path676': book.routes['Car Alarm Traverse'],
         'path670': book.routes['White Rhino'],
         'path678': book.routes['White Rhino'],
         'path668': book.routes['2 Ton Chevey'],
         'path680': book.routes['2 Ton Chevey'],
         'path666': book.routes['Pup Truck'],
         'path682': book.routes['Pup Truck'],
     })
Topo(name='Car Alarm Uphill Side',
     parent=book.formations['Car Alarm'],
     fileName='carAlarm2.svg',
     size='h',
     description='Car Alarm Uphill Side',
     routes={
         'path824': book.routes['Comp Route'],
         'path863': book.routes['Comp Route'],
         'path851': book.routes['Panic Button'],
         'path861': book.routes['Panic Button'],
         'path857': book.variations['Panic Button Variation'],
         'path859': book.variations['Panic Button Variation'],
     })
Topo(name='Boys in the Woods',
     parent=book.formations['Boys In the Woods'],
     fileName='BITW.svg',
     size='f',
     description='Boys in the Woods and Tree Slab',
     routes={
         'path300': book.routes['Boys in the Woods'],
         'path458': book.routes['Boys in the Woods'],
         'path1485': book.routes['Cuba Gooding'],
         'path460': book.routes['Cuba Gooding'],
         'path400': book.routes['Ice Cubes Shiny Jerry Curl'],
         'path462': book.routes['Ice Cubes Shiny Jerry Curl'],
         'path404': book.routes['Tree Slab'],
         'path464': book.routes['Tree Slab'],
         'path480': book.variations['Cuba Gooding Variation'],
         'path426': book.variations['Cuba Gooding Variation'],
     })
Topo(name='enchilada',
     parent=book.formations['E\'s Boulder'],
     fileName='enchilada.svg',
     size='h',
     description='Enchilada',
     routes={
         'path848': book.routes['Enchilada'],
         'path902': book.routes['Enchilada'],
     })
Topo(name='Slam dunk',
     parent=book.formations['E\'s Boulder'],
     fileName='eboulder2.svg',
     size='h',
     description='Slam dunk',
     routes={
         'path1489': book.routes['Slam Dunk'],
         'path1487': book.routes['Slam Dunk'],
     })
Topo(name='Gargoyle',
     parent=book.formations['E\'s Boulder'],
     fileName='eboulder3.svg',
     size='h',
     description='Gargoyle',
     routes={
         'path1625': book.routes['Gargoyle'],
         'path1627': book.routes['Gargoyle'],
         'path1631': book.variations['Gargoyle Direct'],
         'path1629': book.variations['Gargoyle Direct'],
         'path1635': book.routes['Slam Dunk'],
         'path1633': book.routes['Slam Dunk'],
     })
Topo(name='Zen Koan',
     parent=book.formations['Zen Koan'],
     fileName='koan.svg',
     size='h',
     description='Zen Koan',
     routes={
         'path1777': book.routes['Zen Koan'],
         'path1775': book.routes['Zen Koan'],
     })
Topo(name='Night Crawler',
     parent=book.formations['Night Crawler'],
     fileName='nightCrawler.svg',
     size='h',
     description='Night Crawler',
     routes={
         'path1342': book.routes['Night Crawler'],
         'path1396': book.routes['Night Crawler'],
     })
Topo(name='Jesus',
     parent=book.formations['Meth Lab Front Side'],
     fileName='jesus.svg',
     size='f',
     description='Methlab East Face',
     routes={
         'path1908': book.routes['Don\'t Blow the Jug'],
         'path1910': book.routes['Don\'t Blow the Jug'],
         'path1906': book.routes['Trust Issues'],
         'path1912': book.routes['Trust Issues'],
         'path1902': book.routes['Leave it to Jesus'],
         'path1916': book.routes['Leave it to Jesus'],
         'path1904': book.variations['Leave it to Jesus Sit Start'],
         'path1914': book.variations['Leave it to Jesus Sit Start'],
         'path736': book.variations['Leave it to Jesus Left'],
         'path734': book.variations['Leave it to Jesus Left'],
     })
Topo(name='Methlab Backside',
     parent=book.formations['Meth Lab Back Side'],
     fileName='Methlab.svg',
     size='f',
     description='Meth Lab backside',
     routes={
         'path1874': book.routes['Smackdown'],
         'path1856': book.routes['Smackdown'],
         'path1876': book.variations['Harbor Freight'],
         'path1856-2': book.variations['Harbor Freight'],
         'path1878': book.routes['Heisenburg'],
         'path1858': book.routes['Heisenburg'],
         'path1880': book.variations['Learys Lunge'],
         'path1860': book.variations['Learys Lunge'],
         'path1886': book.routes['Octernal'],
         'path1864': book.routes['Octernal'],
         'path1884': book.routes['Guillotine'],
         'path1866': book.routes['Guillotine'],
         'path1888': book.variations['Octernal Center Exit'],
         'path1868': book.variations['Octernal Center Exit'],
         'path1890': book.variations['Octernal Direct Exit'],
         'path1862': book.variations['Octernal Direct Exit'],
         'path1892': book.routes['E\'s'],
         'path1872': book.routes['E\'s'],
     })
Topo(name='octernal2',
     parent=book.formations['Meth Lab Back Side'],
     fileName='octurnal2.svg',
     size='h',
     description='Meth Lab across from E\'s',
     routes={
         'path3604': book.routes['Two Blows One Stroke'],
         'path3553': book.variations['Octernal Direct Exit'],
         'path3608': book.routes['Two Blows One Stroke'],
         'path3606': book.variations['Octernal Direct Exit'],
     })
Topo(name='Locksmith',
     parent=book.formations['Locksmith'],
     fileName='locksmith.svg',
     size='h',
     description='The Locksmith',
     routes={
         'path1894': book.routes['Locksmith'],
         'path1898': book.routes['Locksmith'],
         'path1896': book.variations['Brain Haemorrhage'],
         'path1900': book.variations['Brain Haemorrhage'],
     })
Topo(name='arboretum',
     parent=book.formations['Garden Roof'],
     fileName='arboretum.svg',
     size='h',
     description='Routes on the Garden Roof',
     routes={
         'path501': book.routes['Garden Variety'],
         'path505': book.routes['Garden Project'],
         'path293': book.routes['The Arboretum'],
         'path349': book.routes['The Other Bernd'],
         'path512': book.routes['Garden Variety'],
         'path510': book.routes['Garden Project'],
         'path508': book.routes['The Arboretum'],
         'path508-1': book.routes['The Other Bernd'],
     })
Topo(name='siren',
     parent=book.formations['Gumby Wall'],
     fileName='siren.svg',
     size='h',
     description='The Siren',
     routes={
         'path5162': book.variations['The Siren Stand Start'],
         'path4111': book.routes['The Siren'],
         'path4117': book.routes['Gumby Arete'],
         'path4212': book.routes['The Other Bernd'],
         'path4115': book.variations['Bag of Tricks'],
         'path4175': book.routes['The Siren'],
         'path4175-8': book.routes['Gumby Arete'],
         'path4175-8-6': book.routes['The Other Bernd'],
         'path4175-2': book.variations['Bag of Tricks'],
         'path4175-8-6-6': book.variations['The Siren Stand Start'],
     })
Topo(name='Gumby',
     parent=book.formations['Gumby Wall'],
     fileName='gumby.svg',
     size='h',
     description='Gumby Slab',
     routes={
         'path1571': book.variations['Bag of Tricks'],
         'path1573': book.variations['Bag of Tricks'],
         'path1678': book.variations['Bag of Tricks'],
         'path1569': book.routes['Gumby Arete'],
         'path1676': book.routes['Gumby Arete'],
         'path1563': book.routes['Gumby Slab'],
         'path1674': book.routes['Gumby Slab'],
     })
Topo(name='Mini Me 3',
     parent=book.formations['Mini Me'],
     fileName='miniMe3.svg',
     size='h',
     description='Mini Me',
     routes={
         'path1844': book.routes['Dr. Evil'],
         'path1842': book.routes['Dr. Evil'],
         'path1850': book.routes['Dr. Evil'],
         'path1846': book.routes['Austin Powers'],
         'path1852': book.routes['Austin Powers'],
         'path1848': book.routes['Mini Me'],
         'path1854': book.routes['Mini Me'],
     })
Topo(name='Office',
     parent=book.formations['The Office'],
     fileName='office.svg',
     size='h',
     description='The Office',
     routes={
         'path1834': book.routes['Daryl Philbin'],
         'path1838': book.routes['Daryl Philbin'],
         'path1836': book.routes['Jim Halpert'],
         'path1840': book.routes['Jim Halpert'],
     })
Topo(name='Swollen Member',
     parent=book.formations['Swollen Member'],
     fileName='swollen2.svg',
     size='h',
     description='Swollen Member and Meth Lab High Ball',
     routes={
         'path1813': book.routes['Meth Lab Highball'],
         'path2042': book.routes['Meth Lab Highball'],
         'path1830': book.variations['Meth Lab Highball Sit Start'],
         'path2040': book.variations['Meth Lab Highball Sit Start'],
         'path1832': book.routes['Meth Lab Highball Right'],
         'path2044': book.routes['Meth Lab Highball Right'],
         'path1760': book.routes['Swollen Member'],
         'path1811': book.routes['Swollen Member'],
         'path2046': book.routes['Swollen Member'],
     })
Topo(name='Toilet Bowl',
     parent=book.formations['Toilet Bowl'],
     fileName='toiletBowl.svg',
     size='h',
     description='Toilet Bowl',
     routes={
         'path1752': book.routes['Toilet Bowl'],
         'path1756': book.routes['Toilet Bowl'],
         'path1754': book.routes['Toilet Bowl Traverse'],
         'path1758': book.routes['Toilet Bowl Traverse'],
     })
Topo(name='Tonsil',
     parent=book.formations['Tonsil'],
     fileName='tonsil.svg',
     size='h',
     description='Tonsil',
     routes={
         'path1686': book.routes['Tonsil'],
         'path1688': book.routes['Tonsil'],
         'path1696': book.routes['Tonsil'],
         'path1680': book.routes['All Sorts of Ease'],
         'path1690': book.routes['All Sorts of Ease'],
         'path1682': book.routes['In the Shadow of Giants'],
         'path1692': book.routes['In the Shadow of Giants'],
         'path1684': book.routes['Gingiva'],
         'path1694': book.routes['Gingiva'],
         'path716': book.variations['Prowed'],
         'path566': book.variations['Prowed'],
     })
Topo(name='Trust',
     parent=book.formations['Tyler Durten'],
     fileName='trust.svg',
     size='h',
     description='Trust and Tyler Durten',
     routes={
         'path678': book.routes['Trust'],
         'path830': book.routes['Trust'],
         'path776': book.variations['Iron Cross'],
         'path832': book.variations['Iron Cross'],
         'path834': book.routes['Project Mayhem'],
         'path836': book.routes['Project Mayhem'],
         'path838': book.variations['Tyler Durten Dyno'],
         'path840': book.variations['Tyler Durten Dyno'],
         'path298': book.routes['Angel Face'],
         'path410': book.routes['Angel Face'],
         'path302': book.routes['Durten Layback'],
         'path412': book.routes['Durten Layback'],
     })
Topo(name='Turtle',
     parent=book.formations['Turtle Shell Boulder'],
     fileName='turtle.svg',
     size='h',
     description='Turtle Shell',
     routes={
         'path855': book.routes['Raphael Crack'],
         'path861': book.routes['Raphael Crack'],
         'path857': book.routes['Donatello'],
         'path863': book.routes['Donatello'],
         'path859': book.routes['Leonardo'],
         'path919': book.routes['Leonardo'],
     })
Topo(name='Undertow',
     parent=book.formations['Undertow'],
     fileName='undertow.svg',
     size='h',
     description='Undertow downhill face',
     routes={
         'path1097': book.routes['Undertow'],
         'path1111': book.routes['Undertow'],
         'path1099': book.variations['Spray Against the Undertow'],
         'path1105': book.variations['Spray Against the Undertow'],
         'path1101': book.variations['Undertow Sit Start'],
         'path1107': book.variations['Undertow Sit Start'],
         'path1103': book.routes['Riptide'],
         'path1109': book.routes['Riptide'],
     })
Topo(name='Undertow2',
     parent=book.formations['Undertow'],
     fileName='undertow2.svg',
     size='f',
     description='Undertow East face',
     routes={
         'path932': book.routes['Silly Steep Mantle'],
         'path942': book.routes['Silly Steep Mantle'],
         'path938': book.routes['Undertow'],
         'path946': book.routes['Undertow'],
         'path934': book.variations['Spray Against the Undertow'],
         'path944': book.variations['Spray Against the Undertow'],
         'path936': book.variations['Undertow Sit Start'],
         'path950': book.variations['Undertow Sit Start'],
         'path1134': book.routes['Riptide'],
         'path948': book.routes['Riptide'],
         'path940': book.routes['Tidepool'],
         'path952': book.routes['Tidepool'],
         'path1309': book.routes['Simple Math'],
         'path1305': book.routes['Simple Math'],
         'path1307': book.variations['Shake it Out'],
         'path748': book.variations['Shake it Out'],
     })
Topo(name='Baseball',
     parent=book.formations['Baseball'],
     fileName='baseball.svg',
     size='h',
     description='Baseball',
     routes={
         'path349': book.routes['Baseball'],
         'path293': book.routes['Baseball'],
         'path351': book.routes['Bunt'],
         'path295': book.routes['Bunt'],
     })
Topo(name='Bread Loaf',
     parent=book.formations['Bread Loaf'],
     fileName='breadLoaf.svg',
     size='h',
     description='Bread Loaf',
     routes={
         'path543': book.routes['Bread Loaf Left'],
         'path1100': book.routes['Bread Loaf Left'],
         'path1104': book.routes['Bread Loaf Traverse'],
         'path1153': book.routes['Bread Loaf Traverse'],
         'path1155': book.variations['Baker\'s Dozen'],
         'path1157': book.variations['Baker\'s Dozen'],
     })
Topo(name='Bread Loaf2',
     parent=book.formations['Bread Loaf'],
     fileName='breadLoaf2.svg',
     size='h',
     description='Bread Loaf 2',
     routes={
         'path1350': book.routes['Worf'],
         'path1348': book.routes['Worf'],
         'path1346': book.routes['Worf'],
     })
Topo(name='Scratch and Spliff',
     parent=book.formations['Scratch and Spliff'],
     fileName='scratchSpliff.svg',
     size='h',
     description='Scratch and Spliff',
     routes={
         'path1921': book.routes['Spliff'],
         'path1919': book.routes['Spliff'],
         'path1925': book.routes['Scratch and Spliff Traverse'],
         'path1923': book.routes['Scratch and Spliff Traverse'],
         'path1917': book.routes['Roach'],
         'path1915': book.routes['Roach'],
         'path2515': book.routes['For What it\'s Worth'],
         'path2513': book.routes['For What it\'s Worth'],
     })
Topo(name='Scratch and Spliff 2',
     parent=book.formations['Scratch and Spliff'],
     fileName='scratchSpliff2.svg',
     size='f',
     description='Scratch and Spliff 2',
     routes={
         'path2067': book.routes['Scratch and Spliff Traverse'],
         'path2065': book.routes['Scratch and Spliff Traverse'],
         'path2080': book.routes['Spliff'],
         'path2075': book.routes['Spliff'],
         'path2077': book.routes['Scratch'],
         'path2073': book.routes['Scratch'],
         'path2071': book.variations['Late Start'],
         'path2069': book.variations['Late Start'],
     })
Topo(name='Scratch and Spliff 3',
     parent=book.formations['Scratch and Spliff'],
     fileName='scratchSpliff3.svg',
     size='h',
     description='Scratch and Spliff 3',
     routes={
         'path2226': book.routes['Caliban\'s War'],
         'path2224': book.routes['Caliban\'s War'],
         'path2222': book.routes['Caliban\'s War'],
         'path2228': book.routes['Stoned Age'],
         'path2230': book.routes['Stoned Age'],
     })
AreaMap(name='The Garden Main Area Overview',
        parent=book.areas['The Garden Main'],
        fileName='Garden.svg',
        sub_areas={
            'rect2027': book.subareas['Big'],
            'rect1376': book.subareas['Azain'],
            'rect2313': book.subareas['Entrance Area'],
            'rect2908': book.subareas['Big Fred'],
            'rect3027': book.subareas['Fight Club'],
            'rect3200': book.subareas['Meth Lab'],
            'rect3386': book.subareas['Undertow'],
        },
        layers=['Base'],
        size='f',
        description='The Garden Main Area Overview',)
AreaMap(name='Armageddon Area Overview',
        parent=book.areas['Upper Garden'],
        fileName='upperGarden.svg',
        sub_areas={
            'rect27128': book.subareas['The Bread Loaves/Scratch and Spliff'],
            'rect27051': book.subareas['entranceUpper'],
        },
        layers=['Base', 'border'],
        border='rect27048',
        size='f',
        description='The Garden Main Area Overview',)
SubAreaMap(name='Entrance Area map',
           parent=book.subareas['Entrance Area'],
           outFileName='entrance.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Entrance', 'Base'],
           border='rect2313',
           description='Entrance Area map',
           routes={
           'path1767': book.routes['Toilet Bowl Traverse'],
           'path1769': book.routes['Toilet Bowl'],
           'path1771': book.routes['Donatello'],
           'path1773': book.routes['Leonardo'],
           'path1775': book.routes['Raphael Crack'],
           'path1777': book.routes['Overhand'],
           'path1779': book.routes['Three Star Ledge'],
           'path1781': book.routes['All Sorts of Ease'],
           'path1783': book.routes['In the Shadow of Giants'],
           'path1785': book.routes['Tonsil'],
           'path1787': book.routes['Boys in the Woods'],
           'path1789': book.routes['Ice Cubes Shiny Jerry Curl'],
           'path1791': book.routes['Tree Slab'],
           })
SubAreaMap(name='Fight Club Area map',
           parent=book.subareas['Fight Club'],
           outFileName='fightClub.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Fight Club', 'Base'],
           border='rect3027',
           description='Fight Club Area map',
           size='f',
           routes={
           'path4077': book.routes['E\'s Dirty B'],
           'path1519': book.routes['Jim Halpert'],
           'path1517': book.routes['Daryl Philbin'],
           'path1515': book.routes['Vince'],
           'path1513': book.routes['The Ear'],
           'path1511': book.routes['Fight Club 2'],
           'path1509': book.routes['Project Mayhem'],
           'path1507': book.routes['Trust'],
           'path1505': book.routes['Austin Powers'],
           'path1503': book.routes['Dr. Evil'],
           })
SubAreaMap(name='Undertow area map',
           parent=book.subareas['Undertow'],
           outFileName='undertow.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Undertow', 'Base'],
           border='rect3386',
           description='Undertow area map',
           routes={
               'path1244': book.routes['Silly Steep Mantle'],
               'path1246': book.routes['Undertow'],
               'path1248': book.routes['Tidepool'],
               'path1250': book.routes['Chockstone Highball'],
               'path1252': book.routes['Car Alarm Traverse'],
               'path1254': book.routes['2 Ton Chevey'],
               'path1256': book.routes['Pup Truck'],
               'path1258': book.routes['Comp Route'],
               'path1260': book.routes['Panic Button'],
               'path3384': book.routes['Zen Koan'],
           })
SubAreaMap(name='Meth Lab area map',
           parent=book.subareas['Meth Lab'],
           outFileName='methLab.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Meth Lab', 'Base'],
           border='rect3200',
           description='Meth Lab area map',
           routes={
               'path760': book.routes['Don\'t Blow the Jug'],
               'path762': book.routes['Trust Issues'],
               'path764': book.routes['Leave it to Jesus'],
               'path766': book.routes['Smackdown'],
               'path768': book.routes['Heisenburg'],
               'path770': book.routes['Guillotine'],
               'path772': book.routes['Octernal'],
               'path774': book.routes['Two Blows One Stroke'],
               'path776': book.routes['E\'s'],
               'path778': book.routes['Enchilada'],
               'path780': book.routes['Swollen Member'],
               'path782': book.routes['Meth Lab Highball'],
               'path784': book.routes['The Bubbler'],
               'path4341': book.routes['Meth Lab Project'],
               'path426': book.routes['Slam Dunk'],
               'path428': book.routes['Gargoyle'],
           })
SubAreaMap(name='Big area map',
           parent=book.subareas['Big'],
           outFileName='big.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           description='Big area map',
           routes={
               'path5664': book.routes['Frontside Baldo'],
               'path5662': book.routes['Hueco Wabo'],
               'path5660': book.routes['All Bernd Up'],
               'path410': book.routes['Mini Hydro Tube'],
               'path5658': book.routes['Bitchin Corners'],
               'path5658-4': book.routes['Smol'],
           },
           layers=['Big', 'Base'],
           border='rect2027'),
SubAreaMap(name='Azain area map',
           parent=book.subareas['Azain'],
           outFileName='azain.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           description='Azain area map',
           size='f',
           routes={
               'path738': book.routes['Gumby Crack'],
               'path736': book.routes['Gumby Slab'],
               'path734': book.routes['Gumby Arete'],
               'path732': book.routes['The Siren'],
               'path730': book.routes['Garden Variety'],
               'path728': book.routes['The Arboretum'],
               'path726': book.routes['Full Stroke'],
               'path724': book.routes['Philanthropy'],
               'path722': book.routes['Locksmith'],
               'path720': book.routes['Ground up Blowie'],
               'path718': book.routes['Night Crawler'],
               'path716': book.routes['The Good Slab'],
               'path714': book.routes['The Good'],
               'path712': book.routes['Another'],
               'path710': book.routes['Snakes and Martyrs'],
               'path708': book.routes['Next to the Good'],
               'path740': book.routes['Into the Light'],
               'path742': book.routes['Azain Crack'],
           },
           layers=['Azain', 'Base'],
           border='rect1376')
SubAreaMap(name='Big Fred area map',
           parent=book.subareas['Big Fred'],
           outFileName='Big Fred.png',
           fileName='Garden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Big Fred', 'Base'],
           border='rect2908',
           description='Big Fred area map',
           routes={
               'path714-5': book.routes['Angry Grandma'],
               'path712-7': book.routes['Angry Mom'],
               'path712-6': book.routes['Easy Grandma'],
               'path710-5': book.routes['Big Fred'],
           })
SubAreaMap(name='Entrance area map',
           parent=book.subareas['entranceUpper'],
           outFileName='entranceUpper.png',
           fileName='upperGarden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Entrance', 'Base'],
           border='rect27051',
           description='Entrance area map',
           routes={
               'path27105': book.routes['Pumpkin Spice'],
               'path27107': book.routes['Baseball'],
               'path27109': book.routes['Bunt'],
           })
SubAreaMap(name='Bread loaf/Scratch and Spliff area map',
           parent=book.subareas['The Bread Loaves/Scratch and Spliff'],
           outFileName='bread.png',
           fileName='upperGarden.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Bread', 'Base'],
           border='rect27128',
           size='f',
           description='Bread loaf/Scratch and Spliff area map',
           routes={
               'path27126': book.routes['Caliban\'s War'],
               'path27124': book.routes['Scratch'],
               'path27122': book.routes['Spliff'],
               'path27120': book.routes['Scratch and Spliff Traverse'],
               'path27118': book.routes['For What it\'s Worth'],
               'path27116': book.routes['Worf'],
               'path27114': book.routes['Bread Loaf Traverse'],
               'path27112': book.routes['Bread Loaf Left'],
           })
SubAreaMap(name='Redneck Riviera area map',
           parent=book.subareas['Redneck Riviera'],
           fileName='redneck.svg',
           path_i='./maps/area/',
           path_o='./maps/area/',
           layers=['Redneck', 'Base'],
           border='rect3479',
           size='h',
           description='Redneck Riviera area map',
           routes={
               'path3423': book.routes['Pony Boy'],
               'path3421': book.routes['Monorail Project'],
               'path3419': book.routes['Ugly Face'],
               'path3417': book.routes['Binding of Isaac'],
               'path3415': book.routes['Moss Boss'],
               'path3413': book.routes['Chicken Tendies'],
               'path3411': book.routes['Teenage Libertarians'],
               'path3357': book.routes['Falcon\'s Reach'],
           })
           
           
if __name__ == '__main__':
    sys.exit()