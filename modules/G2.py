from IPython.display import Javascript, display_html


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




# Chart class to be developed
class Chart:
    # Chart object contains all properties and behaviours of a class
    
    def __init__(self, **config_dict):
        
        
        self.layout = config_dict
        self.layout['container'] = 'element.get(0)'
        
    def data(self,data):
        
        self.data = data
        
        
    def render(self):
        # Should be modified in a better form
        layout_code = ('var chart = new G2.Chart(%s);'%self.layout).replace('\'element.get(0)\'','element.get(0)')
        data_code = 'var data = %s; \n chart.data(data);'%self.data
        item_code = 'chart.interval().position(\'x*y\');'
        element_code = ''
        render_code = 'chart.render();'
        
        
        
        final_code = layout_code+data_code+item_code+element_code+render_code
        return Javascript(get_notebook_code(final_code))
        
   



    