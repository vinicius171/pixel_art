# Pixel_art
    o intuito desse código é processar uma imagem para ganhar um aspecto de pixel art
    esse código contem dois filtros para imagens

# Funções
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

![um exemplo da aplicação da primeira tecnica da imagem da Deusa kali](https://i.ibb.co/4dBd1FW/Captura-de-tela-2024-07-01-153742.png)

	def posterize_image(image_path, output_folder, num_colors)
{
A posterização reduz o número de cores em uma imagem, criando um efeito de cores sólidas e distintas
}
> essa função é separada do restante do código, não utiliza nenhuma das funções abordadas anteriormente

![um exemplo da aplicação da segunda tecnica da imagem da Deusa kali](https://i.ibb.co/540qfsQ/Captura-de-tela-2024-07-01-153718.png) 

# Fontes

* https://www.youtube.com/watch?v=CHxXL7A8ZpY&list=PLFLRQZXTN0Bib3eMsOVFeWsBKdevPz5xZ&index=6 (muito importante para entender como funciona o processo de transformar uma imagem normal em pixel arte)
* https://www.cambridgeincolour.com/tutorials/image-interpolation.htm
* https://medium.com/cwi-software/entendendo-clusters-e-k-means-56b79352b452
