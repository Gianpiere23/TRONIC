'''Sistema de gestion de biblioteca por lo menos 2 clases libro y biblioteca
*la clase libreo debe tener titulo autor año de publicaciones y si esta disponible o no 
ademas la clase libro debe de tener prestar, devolver, mostras imforacion'
en
* la clase bibliteca debe tener lista de libros agregar libro,mostrar 
invetario y buscar libro
'''




class biblioteca:
             
 class libro:
     def __init__ (self,titulo,autor,año,disponible,imformacion):
        self.titulo=titulo
        self.autor=autor
        self.año=año
        self.disponible=disponible
        self.imformacion=imformacion

 libro1=libro("Lazarillo de thormes","Cesar vallejo","1990"," Disponible","300")
 libro2=libro("Poemas humanos","Cesar vallejo","2003","Prestado","500")
 libro3=libro("Trilce","Cesar Vallejo","2000"," Disponible","600")
 print("Buenas tardes, esta es mi biblioteca virtual cual de los libros desea usted")
 
 
 contador=0
 
 while contador<3:
         
  print("Libros:\n1.-Lazarillo de thormes\n2.-Poemas humanos\n3.-Trilce\nLibro agregado")
  print("Eliga el numero del libro que usted desea:")
    
  y=(input("-->"))
  if y=="1":
     print(f"Este es el libro : {libro1.titulo}\nSu autor fue: {libro1.autor}")
     print("Desea tener mas imformaicon del libro digite 'SI' ")
     x=input("-->")
     if x=="SI":
      print(f"Este libro fue creado en el año :{libro1.año}\nEste libro se encuentra :{libro1.disponible}\nEste libro contiene:{libro1.imformacion} paginas")
      print("-"*30)
      print("Desea ver otros libros digite la palabra 'SI' ")
      j=input("-->")
      if j=="SI":       
       contador+=1
       continue
      else:
              print("muchas gracias ")
              break
     else:
        print("Muchas gracias por su atencion" )  
        break 
            
 
           
        
  elif y=="2":
       print(f"Este es el libro : {libro2.titulo}\nSu autor fue: {libro2.autor}")
       print("Desea tener mas imformaicon del libro digite 'SI' ")
       x=input("-->")
       if x=="SI":
        print(f"Este libro fue creado en el año :{libro2.año}\nEste libro se encuentra:{libro2.disponible}\nEste libro contiene:{libro1.imformacion} paginas")
        print("-"*30)
        print("Desea ver otros libros digite la palabra 'SI' ")
        j=input("-->")
        if j=="SI":
         contador+=1
         continue
        else:
                print("muchas gracias")
                break
       else:
        print("Muchas gracias por su atencion" )   
        break   
       
    
  elif y=="3":
        print(f"Este es el libro : {libro3.titulo}\nSu autor fue: {libro3.autor}")
        print("Desea tener mas imformaicon del libro digite 'SI' ")
        x=input("-->")
        if x=="SI":
         print(f"Este libro fue creado en el año :{libro3.año}\nEste libro se encuentra:{libro3.disponible}\nEste libro contiene:{libro1.imformacion} paginas")
         print("-"*30)
         print("Desea ver otros libros digite la palabra 'SI' ")
         j=input("-->")
         if j=="SI":
          contador+=1
          continue
         else :
                 print("muchas gracias por su atencion")
                 break
        else:
         print("Muchas gracias por su atencion" )   
        
        break     
        
    
  else:
        print("Muchas gracias por su atencion")
        break    


        