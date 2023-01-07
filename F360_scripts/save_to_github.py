#Author-Burhan Qaddoumi
#Description-Export bodies/components as STL/STEP, create GitHub commit, and add commit ID to version description in Fusion360
#Organization-Tetra Bio Distributed
#https://github.com/tetrabiodistributed
#https://www.tetrabio.org/

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        #creates variable 'doc' from active F360 file as <class 'adsk.fusion.FusionDocument'>
        doc :adsk.core.Document = app.activeDocument
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        allComponents = design.allComponents
        
        #collect all components/bodies for export
        
        #FUTURE file export naming via standard part numbering scheme
        
        #export all in collection as STL/STEP
        
        #create GitHub commit and save commit ID
        
        commit = ''
        
        #save F360 file and add commit ID to description notes
        desc = f"Exported and uploaded as GitHub commit {commit}"
        doc_saved = doc.isSaved
        
        if not doc_saved:
          doc.save(desc)
        elif doc_saved:
          #toggle bodies folder visibility to enable new version save
          allComponents[0]._set_isBodiesFolderLightBulbOn(False)
          allComponents[0]._set_isBodiesFolderLightBulbOn(True)
          doc.save(desc)
          
          msg = f"Export complete, add files to {commit} on GitHub and submit Pull Request"
          ui.messageBox(msg, "Finished")
          
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

