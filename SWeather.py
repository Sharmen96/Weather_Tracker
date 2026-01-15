import gradio as gr
import requests

api_key = '7xxxxxxxxxxxxxxxxxxxxxxxx81'

def get_weather(city): 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get('cod') == '404':
        return "City Not Found",

    weather = data ['weather'][0]['main']    
    temperature = data ['main']['temp'] 
 

    return weather, f"{temperature} °C" 

# Crreate the Gradio interface  

demo = gr.Interface(    
    fn=get_weather, 
    inputs=gr.Textbox(label="Enter City Name"),
    outputs=[
             gr.Textbox(label="Weather"), 
             gr.Textbox(label="Temperature (°C)")
             ],    
    title = "Sharmen's Weather App",    
    description="Get the current weather and temperature for any city." 
)

demo.launch(share=True)   
