from IPython.display import Javascript, display_html
import pandas as pd


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
display_html(loading_code,raw=True)


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
        def aestatic(map,**config):
            if config:
                self.item_code += "."+aes+"('%s',%s)"%(map,config)
            else:
                self.item_code += "."+aes+"('%s')"%map
            return self
        return aestatic

    
    
#     def position(self,map):
#         self.item_code += ".position('%s')"%map
#         return self
        




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
        
    def create_item_code(self):
        
        item_code=''
        for i in self.chart_items:
            item_code+=str(i)+';\n'
            
        return item_code
        
    def render(self):
        # Should be modified in a better form
        layout_code = self.get_layout_code()
        data_code = 'var data = %s; \n chart.data(data);'%self.chart_data
        #item_code = 'chart.interval().position(\'x*y\');'
        item_code = self.create_item_code()
        element_code = ''
        additional_code = self.additional_code
        render_code = 'chart.render();'
        
        
        
        
        final_code = layout_code+data_code+item_code+element_code+additional_code+render_code
        return Javascript(get_notebook_code(final_code))
    
    def get_geom_function(self, geom):
        
        def geometry(**config):
            chart_item = ChartItem(geom)
            chart_item.add_code()
            chart_item.attach_config(config)
            self.chart_items.append(chart_item)
            return chart_item
        return geometry
    
   



    