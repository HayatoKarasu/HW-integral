from matplotlib import pyplot as plt

plt.text(0.01, 0.9, '1) Интеграл - это аналог суммы для ', fontsize=15)
plt.text(0.01, 0.8, 'бесконечного числа бесконечно малых', fontsize=15)
plt.text(0.01, 0.7, 'слагаемых.', fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, '2) Чтобы получить предынтегральную', fontsize=15)
plt.text(0.01, 0.8, 'функцию нужно результат вычисления', fontsize=15)
plt.text(0.01, 0.7, 'интеграла дифференцировать.', fontsize=15)
form = r"$\frac{1}{2}x^4-7x^2+3 = (\frac{1}{2}x^4-7x^2+3)' = $"
plt.text(0.01, 0.6, form, fontsize=15)
form = r"$=\frac{1}{2}(x^4)'-7(x^2)'+(3)'=\frac{1}{2}(4x^3)'-7(2x)'+0 = $"
plt.text(0.01, 0.4, form, fontsize=15)
form = r"$= 2x^3 + 14x$"
plt.text(0.01, 0.2, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, '3) Чему равно значение инеграла?', fontsize=15)
form = r"$\int_0^\pi cos(cos x)dx$"
plt.text(0.01, 0.8, form, fontsize=15)
plt.text(0.01, 0.7, 'для начала упростим функцию:', fontsize=15)
form = r"$= cos^2(x) = \int_0^\pi \frac{1+cos2x}{2}dx = \int_0^\pi \frac{cos2x}{2}+1dx$"
plt.text(0.01, 0.6, form, fontsize=15)
plt.text(0.01, 0.5, 'вычислим по отдельности:', fontsize=15)
form = r"$\int_0^\pi cos2x_ dx = \frac{sin(2x)}{2}$"
plt.text(0.01, 0.4, form, fontsize=15)
form = r"$\int_0^\pi 1_ dx = x$"
plt.text(0.01, 0.25, form, fontsize=15)
form = r"$ = \frac{sin(2x)}{4} + x + C(const)$"
plt.text(0.01, 0.1, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, '4) Таблица основных интегралов:', fontsize=15)
form = r"$1. \int x^n dx = \frac{x^{n+1}}{n+1} + C, n≠-1$"
plt.text(0.01, 0.8, form, fontsize=15)
form = r"$2. \int \frac{dx}{x} = ln|x| + C$"
plt.text(0.01, 0.7, form, fontsize=15)
form = r"$3. \int a^x dx = \frac{a^x}{lna} + C$"
plt.text(0.01, 0.6, form, fontsize=15)
form = r"$4. \int e^x dx = e^x + C$"
plt.text(0.01, 0.5, form, fontsize=15)
form = r"$5. \int sin (x) dx = -cos x + C$"
plt.text(0.01, 0.4, form, fontsize=15)
form = r"$6. \int cos (x) dx = sin x + C$"
plt.text(0.01, 0.3, form, fontsize=15)
form = r"$7. \int tg (x) dx = - ln|cosx| + C$"
plt.text(0.01, 0.2, form, fontsize=15)
form = r"$8. \int ctg (x) dx = ln|sinx| + C$"
plt.text(0.01, 0.1, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()
#plt.savefig('tabint1.png')

form = r"$9. \int \frac{dx}{cos^2x} = tgx + C$"
plt.text(0.01, 0.9, form, fontsize=15)
form = r"$10. \int \frac{dx}{sin^2x} = -ctgx + C$"
plt.text(0.01, 0.78, form, fontsize=15)
form = r"$11. \int \frac{dx}{sinx} = ln|tg \frac{x}{2}| + C$"
plt.text(0.01, 0.66, form, fontsize=15)
form = r"$12. \int \frac{dx}{cosx} = ln|tg \left(\frac{x}{2} + \frac{\pi}{4}\right)| + C$"
plt.text(0.01, 0.54, form, fontsize=15)
form = r"$13. \int \frac{dx}{\sqrt{a^2-x^2}} = arcsin \frac{x}{a} + C$"
plt.text(0.01, 0.42, form, fontsize=15)
form = r"$14. \int \frac{dx}{\sqrt{x^2+a^2}} = ln|x + \sqrt{x^2+a^2} | + C$"
plt.text(0.01, 0.3, form, fontsize=15)
form = r"$15. \int \frac{dx}{a^2+x^2} = \frac{1}{a} arctg \frac{x}{a} + C$"
plt.text(0.01, 0.18, form, fontsize=15)
form = r"$16. \int \frac{dx}{x^2-a^2} = \frac{1}{2a} ln|\frac{x-a}{x+a}| + C$"
plt.text(0.01, 0.08, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()
#plt.savefig('tabint2.png')