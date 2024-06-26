import flet as ft
from flet import colors

botoes = [
    {'operador':'AC','fonte': colors.BLACK,'fundo':colors.BLUE_GREY_100 },
    {'operador':'±','fonte': colors.BLACK,'fundo':colors.BLUE_GREY_100 },
    {'operador':'%','fonte': colors.BLACK,'fundo':colors.BLUE_GREY_100 },
    {'operador':'/','fonte': colors.WHITE,'fundo':colors.ORANGE},
    {'operador':'7','fonte': colors.WHITE,'fundo':colors.WHITE24},
    {'operador':'8','fonte': colors.WHITE,'fundo':colors.WHITE24},
    {'operador':'9','fonte': colors.WHITE,'fundo':colors.WHITE24},
    {'operador':'*','fonte': colors.WHITE,'fundo':colors.ORANGE},
    {'operador':'4','fonte': colors.WHITE,'fundo':colors.WHITE24},
    {'operador':'5','fonte': colors.WHITE,'fundo':colors.WHITE24},
    {'operador':'6','fonte': colors.WHITE,'fundo':colors.WHITE24},
    {'operador':'-','fonte': colors.WHITE,'fundo':colors.ORANGE},
    {'operador':'1','fonte': colors.WHITE,'fundo':colors.WHITE24},
    {'operador':'2','fonte': colors.WHITE,'fundo':colors.WHITE24},
    {'operador':'3','fonte': colors.WHITE,'fundo':colors.WHITE24},
    {'operador':'+','fonte': colors.WHITE,'fundo':colors.ORANGE},
    {'operador':'0','fonte': colors.WHITE,'fundo':colors.WHITE24},
    {'operador':'.','fonte': colors.WHITE,'fundo':colors.WHITE24},
    {'operador':'=','fonte': colors.WHITE,'fundo':colors.ORANGE},
    
]

def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 250
    page.window_height = 380
    page.title = 'Calculadora Geison'
    page.window_always_on_top = True
    
    result = ft.Text(value = '0', color = colors.WHITE, size=20)
    
    def calculate(operador, value_at):
        try:
            value = eval(value_at)
            
            if operador == '%':
                value /= 100
            elif operador ==  '±':
                value = -value
        except:
            return 'Error'        
        return value     
        
    def select(e):
        value_at = result.value if result.value not in ('0', 'Error') else '' 
        value = e.control.content.value
        
        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value = '0'
        else:
            if value_at and value_at[-1] in ('/','*','-','+','.'):
                value_at = value_at[:-1]   
            
            value =  value_at + value
            
            if value[-1] in ('=','%','±'):
                value = calculate(operador=value[-1], value_at=value_at)   
                
        result.value = value       
        result.update()     
    
    display = ft.Row(
        width=250,
        controls=[result],
        alignment= 'end',
    )

    bnt = [ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['fonte']),
        width=50,
        height=50,
        bgcolor=btn['fundo'],
        border_radius = 100,
        alignment=ft.alignment.center,
        on_click=select
        
    ) for btn in botoes]
    
    Keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=bnt,
        alignment='end'
    )


    page.add(display, Keyboard)
    
    
    
ft.app(target = main)