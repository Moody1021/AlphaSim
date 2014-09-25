"""Create a gui interface to run a model
    
"""
_author_ = "Moody Ahmad"
_project_ = "Model Simulator"

import tkinter
import model
import queue
import threading

# buttons initializer, label, cmd, col, row, button handler, gui reference
Buttons = [ {"name" : "Start", "funcname" :  "startButton", "col" : 0, "row" : 0, "func" : None, "gui" : None},
            {"name" : "Step", "funcname" :  "stepButton", "col" : 0, "row" : 1, "func" : None, "gui" : None},
            {"name" : "Stop", "funcname" : "stopButton", "col" : 1, "row" : 0, "func" : None, "gui" : None},
            {"name" : "Reset", "funcname" : "resetButton", "col" : 2, "row" : 0, "func" : None, "gui" : None},
            {"name" : "Quit", "funcname" : "quitButton", "col" : 3, "row" : 0, "func" : None, "gui" : None},
            {"name" : "Print", "funcname" : "printButton", "col" : 3, "row" : 1, "func" : None, "gui" : None}
          ]
# entry areas: label, cmd, col, row, handler func, gui reference, entry variable
Input = [ {"label" : "Universe Size", "funcname" : "univSize", "col" : 0, "row" : 2, "func" : None, "gui" : None, "var" : 300 },
          {"label" : "# of Dimensions", "funcname" : "numDim", "col" : 0, "row" : 3, "func" : None, "gui" : None, "var" : 2 },
          {"label" : "# of Agents", "funcname" : "numAgents", "col" : 0, "row" : 4, "func" : None, "gui" : None, "var" : 30 },
        ]
Output = ["Number of Agents", "Number of Alphas"]

class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        """initialze gui by placing widgets as given in data table initializers"""
        self.grid()

        for i in Buttons:
            i["gui"] = self.placeButton(i["name"], i["funcname"], i["col"], i["row"])

        for i in Input:
            i["gui"] = self.placeEntry(i["label"], i["funcname"], i["col"], i["row"], i["var"])

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       

        self.testafter()

    def placeEntry(self, label, cmd, c, r, dflt):
        """placeEntry on grid on column and row and return entry variable name and gui reference"""
        ent = tkinter.Entry(self)
        ent.grid(column=c, row=r, sticky="EW")
        ent.insert(0, dflt)
        setattr(self.__class__, cmd, ent)
        #setattr(self.__class__, cmd, lambda s: s )
        templabel = tkinter.Label(self, text=label, anchor="w",fg="white",bg="blue")
        templabel.grid(column=c+1,row=r,sticky='EW')
        return ent
                            
    def placeButton(self, name, cmd, c, r):
        """Place a button with label name, callback function cmd at col c and row r"""
        button = tkinter.Button(self, text=name, command=getattr(self, cmd))
        button.grid(column=c, row=r)
        return button

    def startModel(self, qfrommodel, qtomodel, size, numa, ndim):
        m = model.model(qfrommodel, qtomodel, size, numa, ndim)

    def startButton(self):
        self.qfrommodel = queue.Queue()
        self.qtomodel = queue.Queue()
        self.qtomodel.put("Start")
        usize = int(self.univSize.get())
        numa = int(self.numAgents.get())
        ndim = int(self.numDim.get())
        modthread = threading.Thread(target=self.startModel, args=(self.qfrommodel, self.qtomodel, usize, numa, ndim))
        modthread.start()
        
    def stepButton(self):
        self.qtomodel.put("Step")
        print("Step button")
        
    def stopButton(self):
        self.qtomodel.put("Stop")
        print("Stop button")

    def resetButton(self):
        self.qtomodel.put("Reset")
        print("Reset button")

    def quitButton(self):
        self.destroy()
        self.quit()
        
    def printButton(self):
        self.qtomodel.put("Alpha")
        print("Print button")
        
    def testafter(self):
        print("After idle call")

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Alpha Model P5')
    app.mainloop()
