---
title: "Unidade 01"
date: 2024-02-17
description: "UD01: Estructuras e linguaxe de JS"
---
Para a mellor aprendizaxe de JS recoméndase os seguintes recursos:
* [MDM Web Doc: Guía de JavaScript](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide)
* [MDM Web Doc:  JavaScript](https://developer.mozilla.org/es/docs/Learn/JavaScript)
* [W3Schools: Javascript Tutorial](https://www.w3schools.com/js/)
* [Learn JavaScript](https://learnjavascript.online/)
* [El Tutorial de JavaScript Moderno](https://es.javascript.info/)

## 1. Fundamentos de JS
### 1.0 Introducción.
En JavaScript, os tipos de datos primitivos son aqueles que non son obxectos e non teñen métodos. Hai 7 tipos primitivos:

* **Number**: Representa tanto números enteros como flotantes. Exemplos inclúen 42 e 3.14. JavaScript usa un único tipo para todos os números, baseado no estándar IEEE 754 para aritmética de punto flotante.

* **String**: Representa secuencias de caracteres, usadas para texto. Podes definir cadeas de texto usando comiñas simples, dobres, ou acentos graves (template literals), por exemplo, 'ola', "mundo" e `¡Ola mundo!`.

* **Boolean**: Ten dous valores posibles, true (verdadeiro) e false (falso), usados para loxística e condicións.

* **Undefined**: Unha variable á que non se lle asignou un valor ten o valor undefined. Tamén é o valor retornado por funcións que non teñen unha declaración return explícita.

* **Null**: Usado para indicar a ausencia deliberada de calquera valor de obxecto. null é considerado un literal en JavaScript e representa un valor nulo.

* **Symbol**: Introducido en ECMAScript 2015 (ES6), o tipo Symbol permite crear identificadores únicos para *propiedades de obxectos. Cada valor do tipo Symbol é único e inmutable.

* **BigInt**: Tamén introducido en versións máis recentes de ECMAScript, BigInt é un tipo de datos que pode representar números enteiros máis grandes que o límite seguro para o tipo Number (Number.MAX_SAFE_INTEGER).

Estes tipos primitivos son inmutables, o que significa que non podes cambiar o valor dun primitivo unha vez que estea creado. Por exemplo, cando modificas unha cadea, en realidade estás creando unha nova cadea, non modificando a orixinal.

