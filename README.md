# pixel_art
    o intuito desse código é processar uma imagem para ganhar um aspecto de pixel art
    nesse código contem dois filtros para imagens, o primeiro é mais complexo!!!

# funções
    def reduce_resolution(image, new_width, new_height)
   
   {
       redimensiona a imagem para uma nova largura e altura especificadas (new_width e new_height).
       criar uma versão reduzida da imagem ajuda no processo de clustering das cores 
   }

    def extract_main_colors(image, num_colors) 

    
  {
   usa o algoritmo K-Means(recomendo olhas as fontes) para agrupar os pixels da imagem em num_colors clusters.
	Os centros desses clusters representam as cores principais da imagem.
	Esses centros são retornados como uma paleta de cores.
 }

    def map_pixels_to_colors(image, color_palette)
    
  {
  mapeia cada pixel da imagem original para a cor mais próxima na paleta de cores.
	Isso cria uma nova imagem onde os pixels são substituídos pelas cores da paleta.
  }

> [!NOTE]
> podemos limitar o numero de  cores da paleta alterando o valor da variavel num_colors = n.

    create_pixel_art(original_image_path, output_path, num_colors)

{
combina os passos anteriores.
	Carrega a imagem original, reduz sua resolução, extrai as principais cores e mapeia os pixels para essas cores.
	A imagem resultante é salva no caminho especificado}



