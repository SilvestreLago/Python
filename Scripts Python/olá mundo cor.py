import ctypes, sys

def printColorizedInWindows(text, color):
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
    for i in range(0, len(color)):
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color[i])
        sys.stdout.write(text)
    # cor padrão é 7, white
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
    
if __name__ == "__main__":
    text = u"Imprimindo texto colorido no MS-DOS"
    color = [0] # número da cor do texto
    printColorizedInWindows(text, color)
