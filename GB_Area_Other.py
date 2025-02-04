import sys
sys.path.insert(1, '../LocalBoulders')
from dataStructure import Area, Subarea, Formation, Route, Variation
from GB_Book import book

Area(name='Other Areas',
     parent=book,
        format_options=['suppress_histogram'],
     description='The following areas are nearby Sweethome and the Garden. They are included here in limited detail either due to their obscurity, the author\'s lack of familiarity, or both.',)
Subarea(name='The Upper Garden Cliffs',
        parent=book.areas['Other Areas'],
        format_options=['suppress_page_break'],
        description='The Upper Garden is borderd by an extensive cliff line which is both longer and (in some places) taller than the Garden Cliffs. Unfortunatly the area around the cliff and the cliff itself are both covered in poison oak. A free rope adorns the cliff above the Dr. Strangelove boulder for anyone who wants it. Said rope exists as the only remenats of a would be delveloper who found himself sorounded by poison oak and gave up, never to return.\n\nSee approach instructions for the Upper Garden.',)
Subarea(name='Highway 11 Pillar',
        parent=book.areas['Other Areas'],
        format_options=['suppress_page_break'],
        gps='44.50089, -122.47419',
        note='Warning the routes on this feature are equiped with "cold shut" bolts. These bolts are often not strong enough to hold weight and should be avoided or only used with extreme caution.',
        description='A ~40\' knob on the side of the road hosts few lines. For more information on this area consult "Rock Climbing Oregon" by  Adam R. Bolf and Benjamin P. Ruef.',)
Subarea(name='Canyon Creek',
        parent=book.areas['Other Areas'],
        format_options=['suppress_page_break'],
        gps='44.39708529718213, -122.44671253776127',
        description='There\'s a little cliff band and a few boulders on the beach at the confluence of Canyon Creek and the Lower Santiam River.\n\nLocated on Highway 20 10 miles east of Quartzville Road. Park in the dirt pullout on the side of the road just east of concrete bridge and across from Canyon Creek Road. Follow feint trails to the river and watch out for poison oak.',)
Subarea(name='Horse Rock',
        parent=book.areas['Other Areas'],
        format_options=['suppress_page_break'],
        gps='44.31343, -122.33943',
        description='A cool tower in the woods with at least one route on it. There are more formations nearby which also hold potential.',)
Subarea(name='Gordon Ridge',
        parent=book.areas['Other Areas'],
        format_options=['suppress_page_break'],
        gps='44.34844, -122.34942',
        description='Sparse deposits solid rock dots the landscape high above the Santiam along Gordon Ridge. This region was developed in the early 2010s but it never caught on in the same way that the Garden did and today very little evidence of climbing remains. The center of this previous wave of development was an area called "The Vines". Being a tallus feild located at high elevation (4000\') this area probably has a slightly different season than the Garden. Any aspiring archeologists looking to rediscover this region can reach out to the author of this book for more information.',)
Subarea(name='The Menagerie Wilderness',
        parent=book.areas['Other Areas'],
        format_options=['suppress_page_break'],
        gps='44.42210107163126, -122.31253942150109',
        description='The Menagrie is one of Oregons strangest and most mysterious climbing areas. A large valley is decorated by several freestanding towers. For more information on this legendary crag seek out "Rock Climbing Western Oregon: Willamette" by Greg Orton.',)
Subarea(name='Santiam Pinnacle',
        parent=book.areas['Other Areas'],
        format_options=['suppress_page_break'],
        gps='44.38945069565184, -122.19593395548975',
        description='The Santiam Pinnacle is a rock tower hidden in the tree\'s just off of Highway 20. It hosts a worthwile 5.6 multipitch as well as a few other more obscure offerings. Rumor has it that this area has seen recent develompent.\n\nLocated on Highway 20 27 miles from Quartzville Road. Park in a small pullout on the south side of the road and look for a trail heading into the trees on the north side of the road.',)
Subarea(name='Iron Mountain',
        parent=book.areas['Other Areas'],
        format_options=['suppress_page_break'],
        description='Iron mountain is a well known hiking trail at the summit of tombstone pass. Although it\'s iconic spire has been climbed it does not see regular traffic for the obvious reason that it is a dangerous choss pile. The greater area has also been identified as having a limited amount of bouldering potential. To date only one boulder is known to have been devloped.',)
Subarea(name='The Needles',
        parent=book.areas['Other Areas'],
        format_options=['suppress_page_break'],
        gps='44.59672447306725, -122.15597149494864',
        description='The Needles is a large formation of basalt pillars located high in the hills south of detroit lake. The walls are arount 100\' tall in some sections.\n\nAndrew Child and Alex Funk went on an expedition to this crag in the Summer of 2018. They climbed a few routes and found no evidence of other climbing, nor any fixed gear that would indicate prior descents. The rock isn\'t as soild as the garden cliffs but it is of good enough quality for climbing, there is substantial potential for adventure trad climbing here. It is possible that this crag was adversely effected by the 2020 wildfires. If you would like to explore this area feel free to reach out to the author of this guide for more information.',)
Formation(name='Big Iron',
          parent=book.subareas['Iron Mountain'],
          gps='44.391455952052134, -122.14586484301212',
          description='This humble boulder may have less to offer than other areas documented in this book, but since it is not far from the road it may be a worthwile stop for those passing through on their way across the Cascades.\n\nLocated on NF-15 approximately 0.8 miles south of highway 20. Look for the boulder amidst a forested cluster of smaller boulders about 50\' off the road on the downhill side.')
Route(name='Big Iron',
      parent=book.formations['Big Iron'],
      grade=5,
      rating=2,
      FA='Andrew Child',
      description='Sit start under the roof in compression with left hand on a sloper rail and right hand pinching a small right angle corner. Crank a few techy moves to a juggy top out. Take caution, the blocky holds on the upper half were solid at the time of this route\'s development in 2023, but there\'s no telling what a few years of freeze thaw cycles will do to them.')
Route(name='No Stone Unturned',
      parent=book.formations['Big Iron'],
      grade=2,
      rating=1,
      FA='Andrew Child',
      description='Sit start with hands matched on a triangle shaped ledge. Climb up and right while trying not to dab.')
Route(name='Wild Roses',
      parent=book.formations['Big Iron'],
      grade=2,
      rating=2,
      FA='Andrew Child',
      description='Squat start with hands matched on a double pinch feature at the center of of the lichen covered scoop. Trending right out of the scoop is a little easier than staying left. Giving this route two stars may be generous.')
Variation(name='Big Iron Direct',
      parent=book.routes['Big Iron'],
      grade=5,
      rating=2,
      FA='Andrew Child',
      description='Start as for Big Iron, but top to the left of the roof.')