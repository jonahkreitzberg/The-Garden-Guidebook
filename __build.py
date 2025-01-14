import sys
from GB_Book import book
from GB_Area_Main import *
from GB_Area_PinkTag import *
from GB_Area_Cliffs import *
from GB_Area_Upper import *
from GB_Area_Quartz import *
from GB_Area_Other import *
from GB_Images import *
# from GB_Images_test import *

if __name__ == '__main__':
    book.paths['LaTeXTemplates'] = '../LocalBoulders/templates/'
    book.paths['LaTeXOut'] = './sections/'
    book.paths['pdf'] = './'
    book.file_name = 'guideBook_print'
    book.format_options.append('blank_page_after_title')
    book.update()
    book.gen()
    book.format_options.remove('blank_page_after_title')
    book.format_options.append('skip_action_photos')
    book.file_name = 'guideBook'
    book.gen()