def f(word):
    if not word:
        return ""
    
    wave = []
    
    for i in range(len(word)):
        
        part = word[:i].lower() + word[i].upper() + word[i+1:].lower()
        wave.append(part)
    
    return "-".join(wave)

if __name__ == "__main__":
    print(f("book"))   
    print(f("water"))
    print(f("ok"))
    print(f("a"))
    print(f(""))