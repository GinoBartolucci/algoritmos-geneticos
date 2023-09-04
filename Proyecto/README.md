# Algoritmos genéticos y técnicas de aprendizaje automático para el entrenamiento de agentes inteligentes en videojuegos arcade

*Universidad Tecnológica Nacional Facultad Regional Rosario, Algoritmos Genéticos*

[Francisco Mendiburu
](https://github.com/MendiburuFrancisco)[Gino Bartolucci
](https://github.com/GinoBartolucci)[Joaquin Betes](https://github.com/JoaquinBetes)

## Abstract

Este trabajo se origina en la intersección de dos campos científicos altamente relevantes en la actualidad: el aprendizaje automático y los algoritmos genéticos. El presente estudio se centra en el juego arcade "Breakout", donde los agentes controlan una paleta para lograr rebotar una pelota y eliminar una pared compuesta de bloques dispuestos en la parte superior de la pantalla. Aunque este juego puede parecer simple, presenta un entorno interactivo y dinámico con desafíos significativos debido a su naturaleza impredecible y rápida. El objetivo principal de este trabajo es investigar cómo la combinación de algoritmos genéticos y técnicas de aprendizaje automático, específicamente NeuroEvolution of Augmenting Topologies (NEAT), puede llevar a la creación de agentes que superen el rendimiento humano en el juego.

### Palabras Clave

Algoritmos genéticos, crossover, redes neuronales, topologías, deep learning.

## Introducción

El problema a resolver radica en desarrollar estrategias automatizadas que permitan a los agentes aprender y adaptarse en tiempo real para maximizar su puntuación en el juego Breakout. Esto implica la identificación de funciones de aptitud adecuadas, la representación eficiente del espacio de búsqueda y la adaptación de operadores genéticos para mantener la diversidad de soluciones. Además, se explorará cómo las redes neuronales, optimizadas mediante NEAT, pueden mejorar la toma de decisiones de los agentes en un entorno de juego interactivo y desafiante. La organización del documento se compone de varias secciones que abordan la fundamentación teórica, la aplicación de los enfoques propuestos, los resultados obtenidos y su análisis.

## Marco teórico

### Introducción al Aprendizaje Automático y Algoritmos Genéticos

El aprendizaje automático, definido como una rama de la inteligencia artificial, permite a los sistemas computacionales aprender patrones y tomar decisiones a partir de datos, mejorando su rendimiento con la experiencia (Mitchell, T. M.)[1]. Los algoritmos genéticos, por otro lado, son una técnica de optimización inspirada en la evolución biológica, que utiliza operadores genéticos como selección, mutación y crossover para mejorar soluciones candidatas en un espacio de búsqueda (Holland, J. H.)[2].

### Redes Neuronales en el Contexto del Problema

Dentro del campo del aprendizaje automático, las redes neuronales han emergido como una herramienta poderosa para abordar problemas complejos y no lineales, como la toma de decisiones en videojuegos (LeCun, Y., et al.)[3]. En el contexto de la investigación sobre el entrenamiento de agentes inteligentes en videojuegos arcade, las redes neuronales ofrecen la capacidad de aprender representaciones y estrategias adaptativas directamente de los datos del juego. La evolución de la topología de las redes neuronales a través de algoritmos genéticos, como NEAT, permite la adaptación de la arquitectura y el rendimiento del agente a lo largo del tiempo, mejorando su capacidad para enfrentar los desafíos cambiantes del juego.

### Topología en una Red Neuronal

La topología en una red neuronal se refiere a la estructura y disposición de las neuronas y conexiones en capas dentro del modelo (Goodfellow, I., et al.)[4]. Es la configuración espacial que determina cómo las neuronas están conectadas entre sí, influyendo en la capacidad de la red para aprender y generalizar patrones complejos (Nielsen)[5]. Una topología puede ser profunda, con varias capas interconectadas, o más superficial con menos capas, y puede incluir conexiones recurrentes o saltos directos entre capas. La elección de la topología es esencial en el diseño de una red neuronal, ya que determina su capacidad para capturar relaciones entre los datos de entrada y producir salidas precisas y significativas.

### Elección de NEAT en el Proyecto

La elección de utilizar NEAT (NeuroEvolution of Augmenting Topologies) se fundamenta en su potencial para abordar problemas de optimización en entornos complejos y dinámicos como los videojuegos (Stanley & Miikkulainen)[6]. La combinación de algoritmos genéticos y redes neuronales a través de NEAT permite la evolución de la topología, adaptación de la arquitectura y el rendimiento del agente a lo largo del proceso de evolución. Su adopción en el entrenamiento de agentes en videojuegos donde las estrategias pueden ser altamente variables presenta una oportunidad prometedora para resolver los desafíos de optimización y toma de decisiones.

## Enfoque del proyecto

El enfoque se basa en la idea de que un agente aprende a tomar decisiones óptimas al interactuar con su entorno y recibir recompensas por sus acciones (Sutton & Barto)[7]. En el contexto de los videojuegos, los agentes aprenden a través de ensayo y error, ajustando sus acciones para maximizar las recompensas acumuladas a lo largo del tiempo. A medida que los agentes exploran y toman decisiones, ajustan sus políticas de acción para mejorar su desempeño en el juego. NEAT permite la evolución de estrategias de juego a través de la adaptación tanto de la topología como de los pesos de las redes neuronales que guían las acciones del agente. Esto proporciona una solución eficaz para entrenar agentes capaces de anticipar la trayectoria de la pelota, optimizar la posición de la paleta y lograr puntuaciones sobresalientes. Los algoritmos genéticos operan en un espacio de búsqueda definido por una población de agentes, donde cada agente representa una estrategia de juego única codificada en su red neuronal. La población evoluciona a lo largo de generaciones, y los operadores genéticos, como crossover y mutación, influyen en la variación y selección de estrategias.

## Resultados y Discusión

Los resultados obtenidos demuestran la efectividad de la combinación de algoritmos genéticos y NEAT en la mejora del rendimiento de los agentes en el juego Breakout. Los agentes entrenados utilizando esta metodología lograron puntuaciones significativamente más altas en comparación con enfoques tradicionales de aprendizaje automático y métodos basados en reglas heurísticas. La capacidad de adaptación de las topologías de red y los pesos de las neuronas neuronales a lo largo de las generaciones permitió a los agentes desarrollar estrategias más sofisticadas y adaptativas para enfrentar situaciones desafiantes en el juego.

## Conclusiones

Este trabajo demostró que la combinación de algoritmos genéticos y técnicas de aprendizaje automático, específicamente NEAT, puede llevar a la creación de agentes capaces de superar el rendimiento humano en juegos arcade. La evolución de las topologías de red y la adaptación de los pesos de las neuronas neuronales permiten a los agentes aprender estrategias efectivas y adaptativas en entornos de juego dinámicos. Este enfoque tiene aplicaciones más allá de los videojuegos y puede utilizarse para abordar una amplia gama de problemas de optimización y toma de decisiones en entornos complejos. La investigación futura puede explorar la aplicación de estas técnicas en otros dominios y evaluar su capacidad para abordar desafíos más amplios en inteligencia artificial y aprendizaje automático.

## Referencias

1. Mitchell, T. M. (1997). Machine Learning. McGraw-Hill Education.
2. Holland, J. H. (1975). Adaptation in Natural and Artificial Systems. University of Michigan Press.
3. LeCun, Y., et al. (2015). Deep Learning. Nature, 521(7553), 436-444.
4. Goodfellow, I., et al. (2016). Deep Learning. MIT Press.
5. Nielsen, M. A. (2015). Neural Networks and Deep Learning: A Textbook. Determination Press.
6. Stanley, K. O., & Miikkulainen, R. (2002). Evolving Neural Networks through Augmenting Topologies. Evolutionary Computation, 10(2), 99-127.
7. Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction. The MIT Press.
8. Togelius, J., Yannakakis, G. N., & Stanley, K. O. (2009). Preface to the special issue on evolutionary and player-adaptive games. IEEE Transactions on Computational Intelligence and AI in Games, 1(1), 1-2.
9. Xie, H., & Zhong, L. (2017). Playing flappy bird with NEAT. In Proceedings of the 2017 IEEE Symposium Series on Computational Intelligence (SSCI) (pp. 1-6).
