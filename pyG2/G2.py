from IPython.display import Javascript, display_html
import pandas as pd
import pkgutil


# Coded by Thamalu Maliththa Piyadigama

loading_code = '''
<script type="text/javascript">
require.config({

            paths: {

                G2: 'https://gw.alipayobjects.com/os/lib/antv/g2/4.0.7/dist/g2.min'

            }
});
require(['G2'], function(G2) {{

            window.G2 = G2;

        }});
</script>

'''

loading_code_1 ='''<script type="text/javascript">
              
        define('G2', function(require, exports, module) {
            %s
        });
        require(['G2'], function(G2) {
            window.G2 = G2;
        });
        
        </script>'''


def get_notebook_code(code):
    ''' Make a javascript code safe to run on notebook (make `element` unambigous) '''

    return '''
(
    function(element){
       %s
}
)(element)'''%code

# Not necessary for a notebook
def get_pyG2_code(plain_code):

    ''' Make G2 library accessible for a code snippet  '''

    return '''require(['G2'],function(G2){
    %s
})'''%plain_code

def run_code(notebook_code):

    ''' Run a javascript code and display output '''
    return Javascript(notebook_code)

# Load G2 into notebook
g2_source = pkgutil.get_data("G2", 'g2/g2.min.js').decode("utf-8")
display_html(loading_code_1%g2_source,raw=True)
#display_html(loading_code,raw=True)


class ChartItem:
    
        
    def __init__(self, name):
        
        aes = ['position','size','color','shape','label','adjust']
        
        self.item_code = 'chart.'
        self.__name = name
        
        for i in aes:
            self.__dict__[i]= self.get_aes_function(i)
        
        
    def add_code(self):
        self.item_code += self.__name + '(%s)'
        
        
    def attach_config(self,config_dict):
        if config_dict:
            self.item_code = self.item_code%config_dict
        else:
            self.item_code = self.item_code%''
                   
    def __str__(self):
        return self.item_code
    
    def get_aes_function(self,aes):
        def aestatic(map,*values,**config):
            if config:
                self.item_code += "."+aes+"('%s',%s)"%(map,config)
            else:
                if values:
                    self.item_code += "."+aes+"('%s',%s)"%(map,list(values))
                else:
                    self.item_code += "."+aes+"('%s')"%map
            return self
        return aestatic

    
    
#     def position(self,map):
#         self.item_code += ".position('%s')"%map
#         return self
        

class CoordinateControl:
    
    def __init__(self,name):
        
        coord_func = ['reflect','rotate', 'scale','transpose']
        
        self.item_code = 'chart.'
        self.__name = name
        
        for i in coord_func:
            self.__dict__[i]= self.get_coord_function(i)
            
    def get_coord_function(self,name):
        def coord_function(*amount):
            
            if name == 'reflect':
                self.item_code += '.%s("%s")'%(name,amount[0])
            elif name == 'rotate':
                self.item_code += '.%s(%s)'%(name,amount[0])
            elif name == 'scale':
                self.item_code += '.%s(%s,%s)'%(name,amount[0],amount[1])
            elif name == 'transpose':
                self.item_code += '.%s()'%name
            elif name == 'translate':
                self.item_code += '.%s(%s,%s)'%(name,amount[0],amount[1])
            else:
                print("Coordinate transformation '%s' is not supported.")
#             if len(amount)==0:
#                 self.item_code += '.%s()'%name
#             elif len(amount)==1:
#                 self.item_code += '.%s(%s)'%(name,amount[0])
#             else:
#                 self.item_code += '.%s(%s)'%(name,list(amount))
            return self
        return coord_function
        
        
    def add_code(self):
        self.item_code += 'coordinate(\''+self.__name+'\')'
        
        
#     def attach_config(self,config_dict):
#         if config_dict:
#             self.item_code = self.item_code%(','+str(config_dict))
#         else:
#             self.item_code = self.item_code%''
            
    def __str__(self):
        
        return self.item_code
    
 
# Objects to contain codes related to annotations
class AnnotationObject:
    
    #annots = ['arc','dataMarker','dataRegion','image','layout','line','region','regionFilter','render','text']
    code = 'chart.annotation().'
    
    def __init__(self):
        
        
        annots = ['arc','dataMarker','dataRegion','image','layout','line','region','regionFilter','render','text']
        
        for i in annots:
            self.__dict__[i] = self.get_annot_function(i)
    
    
    
    def get_annot_function(self,name):
        def annot_function(**config):
            self.code += name+'(%s)'%config
            return self
        return annot_function
    
    def __str__(self):
        
        return self.code
    


# Chart class to be developed
class Chart:
    # Chart object contains all properties and behaviours of a class
    
    #list of chart geom functions
    
    
    def __init__(self, height=500, width=400, **config):
        
        geom = ['point', 'path', 'edge', 'heatmap', 'interval', 'polygon', 'schema', 'line', 'area']
        
        self.layout = config
        self.layout['container'] = 'element.get(0)'
        self.layout['height'] = height
        self.layout['width'] = width
        self.additional_code = ''
        self.chart_items = []
        self.annotate_items = []
        
        self.coordinate_sys = ''
        self.scale_details = []
        self.axis_details = []
        self.tooltip_details = ''
        self.legend_details = ''
        
        
        for i in geom:
            self.__dict__[i]= self.get_geom_function(i)
        
        

            
    def data(self,data):
        if type(data) == list:
            self.chart_data = data
        elif type(data) == pd.core.frame.DataFrame:
            self.chart_data = data.to_dict(orient='record')
        else:
            raise TypeError("Unsupported input data type. Only `pandas.DataFrame` and `list` of `dictionary`s are supported.")
        
    def get_layout_code(self):
        return ('var chart = new G2.Chart(%s);\n'%self.layout).replace('\'element.get(0)\'','element.get(0)')
    
    def add_code(self,js_code):
        self.additional_code += js_code+';'
        
    def coordinate(self,name,**config):
        self.coordinate_sys = CoordinateControl(name)
        self.coordinate_sys.add_code()
        return self.coordinate_sys
    
    def scale(self,variable,**config):
        code = "chart.scale('%s',%s)"%(variable,config)
        self.scale_details.append(code)
        return self
    
    def axis(self,variable,**config):
        code = "chart.axis('%s',%s)"%(variable,config)
        self.scale_details.append(code)
        return self
    
    def create_scale_code(self):
        code = ""
        for i in self.scale_details:
            code += i + ';\n'
        return code
    
    def create_axis_code(self):
        code = ""
        for i in self.axis_details:
            code += i + ';\n'
        return code
        
    def create_item_code(self):
        
        item_code=''
        for i in self.chart_items:
            item_code+=str(i)+';\n'
            
        return item_code
    
    def create_annotation_code(self):
        
        item_code=''
        for i in self.annotate_items:
            item_code+=str(i)+';\n'
            
        return item_code
    
    def tooltip(self,**config):
         self.tooltip_details = "chart.tooltip(%s)"%config
            
    def legend(self,value='',**config):
        if value and config:
            self.legend_details = "chart.legend('%s',%s)"%(value,config)
        elif value:
            self.legend_details = "chart.legend('%s')"%value
        else:
            self.legend_details = "chart.legend(%s)"%config
            
    def annotation(self):
        
        annot_obj = AnnotationObject()
        self.annotate_items.append(annot_obj)
        return annot_obj
    
    def create_annotate_code(self):
        
        item_code=''
        for i in self.annotate_items:
            item_code+=str(i)+';\n'
            
        return item_code
        
    def render(self):
        # Should be modified in a better form
        layout_code = self.get_layout_code()
        data_code = 'var data = %s; \n chart.data(data);'%self.chart_data
        scale_code = self.create_scale_code()
        #item_code = 'chart.interval().position(\'x*y\');'
        axis_code = self.create_axis_code()
        item_code = self.create_item_code()
        coordinate_code = str(self.coordinate_sys) + ';\n'
        tooltip_code = self.tooltip_details+';\n'
        legend_code = self.legend_details + ';\n'
        annotate_code = self.create_annotate_code()
        element_code = ''
        additional_code = self.additional_code
        render_code = 'chart.render();'
        
        
        
        
        final_code = layout_code+data_code+scale_code+axis_code+item_code+coordinate_code+tooltip_code+element_code+legend_code+annotate_code+additional_code+render_code
        return Javascript(get_notebook_code(final_code))
    
    def facet_render(self, shape, **config):
        
        # Should be modified in a better form
        layout_code = self.get_layout_code()
        data_code = 'var data = %s; \n chart.data(data);'%self.chart_data + '\n'
        scale_code = self.create_scale_code()
        #item_code = 'chart.interval().position(\'x*y\');'
        axis_code = self.create_axis_code()
        item_code = self.create_item_code()
        coordinate_code = str(self.coordinate_sys) + ';\n'
        tooltip_code = self.tooltip_details+';\n'
        legend_code = self.legend_details + ';\n'
        annotate_code = self.create_annotate_code()
        element_code = ''
        additional_code = self.additional_code
        render_code = 'chart.render();'
        
        each_view = '(chart)=>{%s}'%item_code
        config['eachView'] = 'each_view'
        
        facet_code = 'chart.facet("%s",%s)'%(shape,config)+';\n'
        facet_code = facet_code.replace("'each_view'",each_view)
        
        
        
        
        final_code = layout_code+data_code+scale_code+axis_code+facet_code+coordinate_code+tooltip_code+element_code+legend_code+annotate_code+additional_code+render_code
        
        return Javascript(get_notebook_code(final_code))
        
    
    def get_geom_function(self, geom):
        
        def geometry(**config):
            chart_item = ChartItem(geom)
            chart_item.add_code()
            chart_item.attach_config(config)
            self.chart_items.append(chart_item)
            return chart_item
        return geometry
    
   
   



    