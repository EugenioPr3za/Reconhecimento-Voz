importar  speech_recognition  como  sr
de  gtts  import  gTTS
de  playsound  importação  playsound

#Função responsavel por falar 
def  cria_audio ( áudio ):
	tts  =  gTTS ( áudio , lang = 'pt-br' )
	#Salva o arquivo de áudio
	tts . save ( 'audios / hello.mp3' )
	print ( "Estou aprendendo o que você disse ..." )
	#Da reproduzir ao áudio
	playsound ( 'audios / hello.mp3' )


#Função responsável por ouvir e reconhecer uma fala
def  ouvir_microfone ():
	#Habilitar o microfone para ouvir o usuário
	microfone  =  sr . Reconhecedor ()
	com  sr . Microfone () como  fonte :
		#Chama uma função de redução de ruido disponível na speech_recognition
		microfone . Adjust_for_ambient_noise ( origem )
		#Avisa ao usuário que está pronto para ouvir
		print ( "Diga alguma coisa:" )
		#Armazena a informação de áudio na variável
		audio  =  microfone . ouvir ( fonte )


	tente :
		#Passa ou áudio para reconhecimento de padrões de fala_reconhecimento
		frase  =  microfone . accept_google ( áudio , idioma = 'pt-BR' )
		# Após alguns segundos, retorna uma frase falada
		print ( "Você disse:"  +  frase )

		#Caso não tenha reconhecido ou bloqueado a fala, registre esta mensagem
	exceto  sr . UnkownValueError :
		print ( "Não entendi" )

	retornar  frase

frase  =  ouvir_microfone ()
cria_audio ( frase )
