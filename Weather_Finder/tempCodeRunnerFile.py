import requests
import tkinter
import tkinter.messagebox
def explore():
 city=txt.get()
 url='http://api.openweathermap.org/data/2.5/weather?appid=71086d73379608f812f1b9e1583b8a98&q='+city
 json_data=requests.get(url).json()
 result='The weather at '+city+' is '+json_data['weather'][0]['description']
 tkinter.messagebox.showinfo('Weather Finder',message=result)

window=tkinter.Tk()
window.title('Weather Finder')
icon=tkinter.PhotoImage(file="C:/Users/USER/Documents/my projects/Weather_Finder/weather.png")
label1=tkinter.Label(window,image=icon)
label1.pack(fill='x')
label2=tkinter.Label(text='Enter the city (ex:Mumbai) :')
label2.pack(fill='y')
txt=tkinter.Entry()
txt.pack(fill='y')
button=tkinter.Button(window,text='Get weather condition',command=explore).pack(fill='y')
window.mainloop()