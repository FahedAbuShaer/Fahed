% Creating the Geometry of the Problem
points = .95*[0 -2.5 0 -1; -2.2 0 0.1 0];
sp = spmak(-4:8,[points points]);
f = fnplt(sp,[0 4]);
pg2 = polyshape(f(1,:)',f(2,:)','Simplify',true);
tr = triangulation(pg2);
plot(pg2)
b = 1;
%%
% Creating the Model for the PDE
model = createpde;
% Feeding it the triangular mesh
model.geometryFromMesh(tr.Points', tr.ConnectivityList')
% Applying Dirichlet BC
% Dirichlet:
% hu=r
% Robin boundary condition % n·(c∇u)+qu=g
applyBoundaryCondition(model,'neumann','Edge',1,'g',1,'q',2);
% applyBoundaryCondition(model,'dirichlet','Edge',1,'u', 0 );
generateMesh(model,"Hmax",0.05);
pdemesh(model)
%%
% Defining the Equation Symbolically [two-dimensional problem u(x,y)]
syms a(x,y,t)
syms b(x,y,t)
syms f(a,b)
syms g(a,b)
syms Da
syms Db
pdeeq1 = -diff(a,t) + Da * laplacian(a,[x, y]) + f;
pdeeq2 = -diff(b,t) + Db * laplacian(b, [x y]) + g;
% Specifying the Coefficients Manually
% This Requires you to follow the below:
% solvepde solves PDEs of the form:
% m∂2u/∂t2 +d∂u/∂t - ∇·(c∇u)+au=f
% solvepdeeig solves PDE eigenvalue problems of the form:
%∇ · (c∇u) + au = λdu
%or
% ∇·(c∇u)+au=λ2mu
% Coefficient can be Specified Automatically
coeffs = pdeCoefficients(pdeeq,u);
specifyCoefficients(model,'m',coeffs.m,'d',1,'c',coeffs.c,'a',coeffs.a,'f',coeffs.f);
r = [-Inf,1000];
% Solving it and Finding the Lowest Eigenvalue
setInitialConditions(model,1);
t_list =0:0.01:0.8;
results = solvepde(model,t_list);
%%
% Creating the Color Map for the Plot
n = 100;
cm_parula = parula(n);

% Plotting the Solution over Time
sol = results.NodalSolution;
figure;
hold all;
for it = 1:length(t_list)
    pdeplot(model, 'XYData', sol(:, it), 'ColorMap', cm_parula, 'Contour', 'on');
    title("Time " + t_list(it))
    pause(0.05)
end