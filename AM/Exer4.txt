import sympy as sp
import numpy as np





#função usada de exemplo
x, y = sp.symbols('x y')
f = x**2 + y**2 - 4*x - 2*y + 5 

var = [x,y]
itera_max_padrao = 1000
tolerancia_padro = 1e-6

primeiro_ponto_padrao = [0,0]

#funções

def gradiente(f, alpha, vars=var, x0=primeiro_ponto_padrao, tolerancia=tolerancia_padro, itera_max=itera_max_padrao):
    
    derivadas = []
    for i in vars:
        derivadas.append(sp.diff(f, i))

    grad_f = sp.Matrix(derivadas)
    xk = np.array(x0, dtype=float)

    grad_f_l = sp.lambdify(vars, grad_f, 'numpy')

    for _ in range(itera_max):
        g = np.array(grad_f_l(*xk), dtype=float).flatten()
        xk1 = xk - alpha * g
        if np.linalg.norm(xk1 - xk) < tolerancia:
            return xk1

        xk = xk1
    raise Exception("não convergiu")





def newton(f, vars=var, x0=primeiro_ponto_padrao, tolerancia=tolerancia_padro, itera_max=itera_max_padrao):
    
    derivadas = []
    for i in vars:
        derivadas.append(sp.diff(f, i))

    grad_f = sp.Matrix(derivadas)
    hess_f = sp.hessian(f, vars)

    grad_f_l = sp.lambdify(vars, grad_f, 'numpy')
    hess_f_l = sp.lambdify(vars, hess_f, 'numpy')


    xk = np.array(x0, dtype=float)

    for _ in range(itera_max):

        g = np.array(grad_f_l(*xk), dtype=float).flatten()
        H = np.array(hess_f_l(*xk), dtype=float)
        
        # resolver o  H * p = g
        p = np.linalg.solve(H, g)
        xk1 = xk - p

        if np.linalg.norm(xk1 - xk) < tolerancia:
            return xk1
        xk = xk1
    raise Exception("não convergiu")




def newton_modificado(f, vars=var, x0=primeiro_ponto_padrao, tolerancia=tolerancia_padro, itera_max=itera_max_padrao, lam=1e-4):


    derivadas = []
    for i in vars:
        derivadas.append(sp.diff(f, i))

    grad_f = sp.Matrix(derivadas)
    hess_f = sp.hessian(f, vars)

    grad_f_l = sp.lambdify(vars, grad_f, 'numpy')
    hess_f_l = sp.lambdify(vars, hess_f, 'numpy')


    xk = np.array(x0, dtype=float)

    for _ in range(itera_max):

        g = np.array(grad_f_l(*xk), dtype=float).flatten()
        H = np.array(hess_f_l(*xk), dtype=float)
        
        #modificação se for negativa
        lam_min = np.linalg.eigvalsh(H)[0]
        val = max(0.0, lam - lam_min) 
        H_mod = H + val * np.eye(H.shape[0])



        # resolver o  H * p = g
        p = np.linalg.solve(H_mod, g)
        xk1 = xk - p

        if np.linalg.norm(xk1 - xk) < tolerancia:
            return xk1
        xk = xk1
    raise Exception("não convergiu")





def levenberg_marquardt(f, vars=var, x0=primeiro_ponto_padrao, tolerancia=tolerancia_padro, itera_max=itera_max_padrao, lam=1e-4):


    derivadas = [sp.diff(f, v) for v in vars]
    grad_f = sp.Matrix(derivadas)
    hess_f = sp.hessian(f, vars)

    grad_f_l = sp.lambdify(vars, grad_f, 'numpy')
    hess_f_l = sp.lambdify(vars, hess_f, 'numpy')


    xk = np.array(x0, dtype=float)

    for _ in range(itera_max):
        g = np.array(grad_f_l(*xk), dtype=float).flatten()
        H = np.array(hess_f_l(*xk), dtype=float)

        H_mod = H + lam * np.eye(H.shape[0])

        #resolver o H * p = g
        try:
            p = np.linalg.solve(H_mod, g)
        except np.linalg.LinAlgError:
            raise Exception("Matriz singular na iteração")

        xk1 = xk - p

        #critério de parada
        if np.linalg.norm(xk1 - xk) < tolerancia:
            return xk1

        xk = xk1

    raise Exception("Não convergiu")




#usei o bfgs para quase-newton
def quase_newton(f, vars=var, x0=primeiro_ponto_padrao, tolerancia=tolerancia_padro, itera_max=itera_max_padrao):


    grad_f = sp.Matrix([sp.diff(f, v) for v in vars])
    grad_f_l = sp.lambdify(vars, grad_f, 'numpy')
    f_l = sp.lambdify(vars, f, 'numpy')

    xk = np.array(x0, dtype=float)
    gk = np.array(grad_f_l(*xk), dtype=float).flatten()


    Bk = np.eye(len(vars))

    for _ in range(itera_max):
        try:
            pk = -np.linalg.solve(Bk, gk)
        except np.linalg.LinAlgError:
            raise Exception("Matriz singular em BFGS")

        x_new = xk + pk
        g_new = np.array(grad_f_l(*x_new), dtype=float).flatten()

        #criterio de parada
        if np.linalg.norm(g_new) < tolerancia:
            return x_new

        #vetores de atualização
        sk = (x_new - xk).reshape(-1, 1)
        yk = (g_new - gk).reshape(-1, 1)

         #atualiza (@ é multiplicação de matrizes)
        denom1 = (yk.T @ sk).item()
        denom2 = (sk.T @ Bk @ sk).item()

        if denom1 > 1e-10 and denom2 > 1e-10:
            Bk = Bk + (yk @ yk.T) / denom1 - (Bk @ sk @ sk.T @ Bk) / denom2


        xk, gk = x_new, g_new

    raise Exception("Não convergiu")





#rodar eles
raiz = gradiente(f,0.01)
print("Minimo achado em gradiente: ", raiz)

raiz = newton(f)
print("Minimo achado em newton: ", raiz)

raiz = newton_modificado(f)
print("Minimo achado em newton modificado: ", raiz)

raiz = levenberg_marquardt(f)
print("Minimo achado em levenberg marquardt: ", raiz)

raiz = quase_newton(f)
print("Minimo achado em quase newton: ", raiz)