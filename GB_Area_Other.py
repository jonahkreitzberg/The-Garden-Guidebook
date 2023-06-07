import sys
sys.path.insert(1, '../LocalBoulders')
from dataStructure import Area, Subarea, Formation, Route, Variation
from GB_Book import book

Area(name='Other Areas',
     parent=book,
     description='The following areas are nearby Sweethome and the Garden. They are included here in limited detail either due to their obscurity, my lack of familiarity, or both.',)
Subarea(name='',
        item_id='Other Areas',
        parent=book.areas['Other Areas'],)
Formation(name='The Upper Garden Cliffs',
          parent=book.subareas['Other Areas'],
          description='The Upper Garden is borderd by an extensive cliff line which is both longer and (in some places) taller than the Garden Cliffs. Unfortunatly thea area around the cliff and the cliff itself are both covered in poison oak. A free rope adorns the cliff above the Dr. Strangelove boulder for anyone who wants it. The only remenats of a would be delveloper who found himself sorounded by poison oak and gave up, never to return.\n\nSee approach instructions for the Upper Garden.',)
Formation(name='Canyon Creek',
          parent=book.subareas['Other Areas'],
          description='There\'s a little cliff band and a few boulders on the beach at the confluence of Canyon Creek and the Lower Santiam River.\n\nLocated on Highway 20 10 miles east of Quartzville Road. Park in the dirt pullout on the side of the road just east of concrete bridge and across from Canyon Creek Road. Follow feint trails to the river and watch out for poison oak.',)
Formation(name='Gordon Ridge',
          parent=book.subareas['Other Areas'],
          description='Sparse deposits solid rock dots the landscape high above the Santiam along Gordon Ridge. This region was developed in the early 2010s but it never caught on in the same way that the Garden did and today very little evidence of climbing remains. The center of this previous wave of development was an area called "The Vines" being a tallus feild located at high elevation (4000\') this area probably has a slightly different season than the Garden. Any aspiring archeologists looking to rediscover this region should reach out for more information.',)
Formation(name='The Menagerie Wilderness',
          parent=book.subareas['Other Areas'],
          description='The Menagrie is one of Oregons strangest and most mysterious climbing areas. A large valley is decorated by several freestanding towers. For more information on this legendary crag seek out "Rock Climbing Western Oregon: Willamette" by Greg Orton.',)
Formation(name='Santiam Pinnacle',
          parent=book.subareas['Other Areas'],
          description='The Santiam Pinnacle is a rock tower hidden in the tree\'s just off of Highway 20. It hosts a worthwile 5.6 multipitch as well as a few other more obscure offerings. Rumor has it that this area has seen recent develompent.\n\nLocated on Highway 20 27 miles from Quartzville Road. Park in a small pullout on the south side of the road and look for a trail heading into the trees on the north side of the road.',)
Formation(name='The Needles',
          parent=book.subareas['Other Areas'],
          description='The Needles is a large formation of basalt pillars located high in the hills south of detroit lake. The walls are arount 100\' tall in some sections.\n\nI went on an expedition to this crag in the Summer of 2018. My climbing partner, Alex Funk, and I climbed a few routes and found no other evidence of other climbing, nor any fixed gear that would indicate prior descents. The rock isn\'t as soild as the garden cliffs but it is of good enough quality for climbing, there is substantial potential for adventure trad climbing here. It is possible that this crag was adversely effected by the 2020 wildfires, I have not been back since the first expedition. If you would like to explore this area feel free to reach out for more information.',)