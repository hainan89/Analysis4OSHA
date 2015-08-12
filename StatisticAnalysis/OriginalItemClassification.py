'''
Created on 2015年8月9日

@author: hainan
'''

class ItemClassification(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    degree_classification = {
        'Non Hospitalized injury': 954, 
        'Non record': 2003, 
        'Hospitalized injury': 6617, 
        'Fatality': 5664
    }    
    
    nature_classification = {
        'Non record': 2003, 
        'Strain/Sprain': 209, 
        'Dermatitis': 2, 
        'Electric Shock': 97, 
        'Poisoning(Systemic)': 3, 
        'Radiation Effects': 1, 
        'Cut/Laceration': 368, 
        'Burn(Chemical)': 9, 
        'Foreign Body Ineye': 4, 
        'Hearing Loss': 2, 
        'Asphyxia': 38, 
        'Puncture': 145, 
        'Amputation': 31, 
        'Other': 2481, 
        'Heat Exhaustion': 4, 
        'Cancer': 16, 
        'Concussion': 1773, 
        'Freezing/Frost Bite': 13, 
        'Dislocation': 143, 
        'Burn/Scald(Heat)': 34, 
        'Hernia': 6, 
        'Fracture': 6607, 
        'Bruise/Contus/Abras': 1249
    }
    
    
    occupation_classification = {
        'Vehicle washers and equipment cleaners': 1, 
        'Truck drivers, heavy': 13, 
        'Supervisors; carpenters and related workers': 174, 
        'Janitors and cleaners': 6, 
        'Freight, stock and material handlers, n.e.c.': 1, 
        'Technicians, n.e.c.': 10, 
        'Crane and tower operators': 19, 
        'Inspectors, testers and graders': 6, 
        'Supervisors, n.e.c.': 119, 
        'Sawing machine operators': 1, 
        'Motor transportation occuputions n.e.c.': 1, 
        'Hoist and winch operators': 1, 
        'Brickmasons and stonemasons': 171, 
        'Helpers, extractive occupations': 3, 
        'Graders and sorters, except agricultural': 1, 
        'Supervisors, production occupations': 3, 
        'Supervisors, cleaning and building service workers': 3, 
        'Science technicians, n.e.c.': 1, 
        'Helpers, construction trades': 130, 
        'Water and sewage treatment plant operators': 1, 
        'Occupational therapists': 1, 
        'Telephone line installers and repairers': 28, 
        'Structural metal workers': 560, 
        'Roofers': 1079, 
        'Excavating and loading machine operators': 7, 
        'Police and detectives, public service': 2, 
        'Groundskeepers and gardeners, except farm': 2, 
        'Truck drivers, light': 2, 
        'Electricians': 236, 
        'Supervisors; brickmasons, stonemasons, tilesetters': 39, 
        'Managers, marketing, advertising, & public rela.': 1, 
        'Civil engineers': 4, 
        'Supervisors and proprietors, sales occupations': 2, 
        'Supervisors; plumbers, pipefitters & steamfitters': 22, 
        'Construction inspectors': 8, 
        'Supervisors, firefighting & fire prevention occupa': 1, 
        'Tool and die makers': 1, 
        'Production helpers': 2, 
        'Hand molders and shapers, except jewelers': 1, 
        'Occupation not reported': 5451, 
        'Industrial engineers': 1, 
        'Welders and cutters': 82, 
        'Tile setters, hard and soft': 13, 
        'Drywall installers': 208, 
        'Miscellaneous material moving equipment operators': 12, 
        'Elevator installers and repairers': 23, 
        'Sheet metal worker apprentices': 7, 
        'Specified mechanics and repairers': 5, 
        'Carpenter apprentices': 125, 
        'Telephone installers and repairers': 7, 
        'Industrial engineering technicians': 1, 
        'Paving, surfacing and tamping equipment operators': 12, 
        'Miscellaneous plant and system operators': 1, 
        'Millwrights': 27, 
        'Forestry workers, except logging': 2, 
        'Supervisors, material moving equipment operators': 1, 
        'Sheetmetal duct installers': 69, 
        'Fire inspection and fire prevention occupations': 2, 
        'Sociology teachers': 1, 
        "Misc. metal,plastic,stone&glass-working; mach. op's": 2, 
        'Data processing equipment repairers': 2, 
        'Supervisors; handlers,equip-cleaners,laborers nec': 18, 
        'Drillers, earth': 6, 
        'Painters, construction and maintenance': 471, 
        'Grader, dozer and scraper operators': 5, 
        'Supervisors, mechanics and repairers': 9, 
        'Political science teachers': 1, 
        'Managers and administrators, n.e.c': 9, 
        'Carpet installers': 4, 
        'Drillers, oil well': 2, 
        'Management related occupations, n.e.c.': 5, 
        'Sales occupations, other business services': 1, 
        'Construction trades, n.e.c.': 522, 
        'Hand painting, coating and decorating occupations': 7, 
        'Miscellaneous hand working occupations': 8, 
        'Industrial truck and tractor equipment operators': 11, 
        'Carpenters': 1394, 
        'Communications equipment operators, n.e.c.': 7, 
        'Supervisors, related agricultural occupations': 1, 
        'Painters, sculptors, craft-artists & printmakers': 3, 
        'Non record': 1620, 
        'Electronic repairers, communica. & indus. equip.': 21, 
        'Insurance adjusters, examiners and investigators': 1, 
        'Misc. electrical & electronic equipment repairers': 12, 
        'Plasterers': 136, 
        'Traffic, shipping and receiving clerks': 1, 
        'Stock handlers and baggers': 1, 
        'Farm workers': 3, 
        'Laborers, except construction': 51, 
        'Adjusters and calibrators': 1, 
        'Cabinet makers and bench carpenters': 2, 
        'Heavy equipment mechanics': 5, 
        'Supervisors, forestry and logging workers': 1, 
        "Supervisors; distrib., sched'g & adjusting clerks": 1, 
        'Sheet metal workers': 50, 
        'Electrical power installers and repairers': 83, 
        'Concrete and terrazzo finishers': 77, 
        'Optometrists': 1, 
        'Construction laborers': 1354, 
        'Mechanical engineers': 2, 
        'Miscellaneous precision workers, n.e.c.': 1, 
        'Insulation Workers': 36, 
        'Miscellaneous precision metal workers': 3, 
        'Mining machine operators': 8, 
        'Electrical and electronic technicians': 24, 
        'Plumbers, pipefitters and steamfitters': 125, 
        'Bus, truck and stationary engine mechanics': 1, 
        "Electricians' apprentices": 79, 
        'Hand packers and packagers': 4, 
        'Sales engineers': 2, 
        'Supervisors, extractive occupations': 1, 
        'Sales workers, hardware and building supplies': 3, 
        'Timber cutting and logging occupations': 2, 
        'Sales counter clerks': 2, 
        'Brickmasons and stonemasons apprentices': 40, 
        'Assemblers': 6, 
        'Painting and paint spraying machine operators': 8, 
        'Heating, air conditioning, and refrig. mechanics': 55, 
        'Engineering technicians, n.e.c.': 3, 
        'Glaziers': 30, 
        'Lay-out workers': 2, 
        'Not specified mechanics and repairers': 15, 
        'Supervisors, food preparation & service occupation': 1, 
        'Boilermakers': 14, 
        'Helpers, mechanics and repairers': 10, 
        'Lathe and turning machine set-up operators': 2, 
        'Trade and industrial teachers': 1, 
        'Machine operators, not specified': 1, 
        'Supervisors; painters, paperhangers and plasterers': 36, 
        'Drilling and boring machine operators': 2, 
        'Plumber, pipefitter and steamfiter apprentices': 49, 
        'Supervisors; electricians & power transm. install.': 17, 
        'Machinery maintenance occupations': 8, 
        'Operating engineers': 3, 
        'Computer systems analysts and scientists': 1, 
        'Hand cutting and trimming occupations': 3, 
        'Precision assemblers, metal': 4, 
        'Supervisors, motor vehicle operators': 2, 
        'Mechanical engineering technicians': 7, 
        'Photographers': 1, 
        'Miscellaneous precision woodworkers': 2
    }
    
    cause_classification = {
        ' Steel Erection Of Solid Web-Welding/Burning/Grindi': 17, 
        ' Cutting concrete pavement': 15, 
        ' Interior carpentry': 297, 
        ' Pouring concrete for piers, and pylons': 8, 
        ' Landscaping': 23, 
        ' Interior plumbing, ducting, electrical work': 177, 
        ' Loading dock forming and pouring': 3, 
        ' Installation Of Decking-Final Attachment Deck (Wel': 21, 
        ' Waterproofing': 54, 
#         ' ': 580, 
        ' Temporary work (buildings, facilities)': 227, 
        ' Interior tile work (ceramic, vinyl, acoustic)': 23, 
        ' Steel Erection Of Open Web Steel Joists-Bolting-Up': 10, 
        ' Steel Erection Of Solid Web-Bolting-Up/Detail Work': 24, 
        ' Fencing, installing lights, signs, etc.': 81, 
        ' Surveying': 16, 
        ' Steel Erection Of Solid Web-Plumbing-Up': 7, 
        ' Other Activities-Installing Ornamental And Archite': 94, 
        ' Dredging': 9, 
        ' Plastering': 132, 
        ' Stripping and curing concrete': 30, 
        ' Erecting structural steel': 403, 
        ' Installing culverts and incidental drainage': 26, 
        ' Pouring concrete floor at grade': 17, 
        ' Steel Erection Of Solid Web-Connecting': 86, 
        ' Installing underground plumbing conduit': 18, 
        ' Trenching, installing pipe': 25, 
        ' Installing equipment (HVAC and other)': 392, 
        ' Interior painting and decorating': 142, 
        ' Installation Of Decking-Hoisting Bundles': 12, 
        ' Exterior painting': 358, 
        ' Bituminous concrete placement': 8, 
        ' Other Activities-Post Decking Detail Work': 118, 
        ' Installation Of Decking-Flashing Of Decking': 18, 
        ' Installing plumbing, lighting fixtures': 186, 
        ' Construction of playing fields, tennis courts': 10, 
        ' Interior masonry': 65, 
        ' Emplacing reinforcing steel': 61, 
        ' Forming': 127, 
        ' Steel Erection Of Open Web Steel Joists-Landing Ma': 8, 
        ' Seawall construction, riprap placement': 2, 
        ' Exterior masonry': 309, 
        ' Traffic protection': 14, 
        ' Site grading and rock removal': 11, 
        ' Swimming pool construction': 4, 
        ' Steel Erection Of Open Web Steel Joists-Welding/Bu': 8, 
        ' Excavation': 35, 
        'Non record': 7095, 
        ' Roofing': 1525, 
        ' Steel Erection Of Open Web Steel Joists-Moving Poi': 6, 
        ' Installing interior walls, ceilings, doors': 318, 
        ' Exterior cladding': 77, 
        ' Installing windows and doors, glazing': 108, 
        ' Elevator, escalator installation': 36, 
        ' Paving': 14, 
        ' Installing metal siding': 92, 
        ' Backfilling and compacting': 17, 
        ' Steel Erection Of Open Web Steel Joists-Plumbing-U': 2, 
        ' Pouring concrete foundations and walls': 51, 
        ' Pouring or installing floor decks': 47, 
        ' Placing bridge deck': 18, 
        ' Fireproofing': 40, 
        ' Pile driving': 6, 
        ' Placing bridge girders and beams': 25, 
        ' Forming for piers or pylons': 15, 
        ' Steel Erection Of Open Web Steel Joists-Connecting': 28, 
        ' Site clearing and grubbing': 36, 
        ' Demolition': 296, 
        ' Installation Of Decking-Initial Laying Deck (Incl': 130, 
        ' Steel Erection Of Solid Web-Moving Point To Point': 9, 
        ' Steel Erection Of Solid Web-Landing Materials (Hoi': 9, 
        ' Erection of coffer dams, caissons': 5, 
        ' Exterior carpentry': 922
    }
    
    fat_cause_classification = {
        ' Struck by falling object/projectile': 45, 
        ' Crushed/run-over by construction equipment during': 3, 
        ' Electrocution from equipment installation/tool use': 7, 
        ' Electric shock, other and unknown cause': 30, 
        ' Unloading-loading equipment/material (except by cr': 3, 
        ' Electrocution by equipment contacting wire': 12, 
        ' Fall through opening (other than roof)': 480, 
        ' Fall from/with bucket (aerial lift/basket)': 176, 
        ' Wall (earthen) collapse': 1, 
        'Non record': 7095, 
        ' Drown, non-lethal fall': 12, 
        ' Crushed/run-over/trapped of operator by operating': 13, 
        ' Fall from vehicle (vehicle/construction equipment)': 102, 
        ' Fire/explosion': 4, 
        ' Fall from/with ladder': 1272, 
#         ' ': 515, 
        ' Electrocution by touching exposed wire/source': 14, 
        ' Fall from/with scaffold': 1093, 
        ' Lifting operations': 2, 
        ' Caught in stationary equipment': 6, 
        ' Asphyxiation/inhalation of toxic vapor': 8, 
        ' Collapse of structure': 193, 
        ' Crushed/run-over by highway vehicle': 2, 
        ' Fall, other': 678, 
        ' Trench collapse': 3, 
        ' Fall from/with platform catwalk (attached to struc': 144, ' Other': 59, 
        ' Heat/hypothermia': 1, 
        ' Elevator (struck by elevator or counter-weights)': 2, 
        ' Crushed/run-over of non-operator by operating cons': 2, 
        ' Fall from/with structure (other than roof)': 1226, 
        ' Fall from roof': 2035
    }    