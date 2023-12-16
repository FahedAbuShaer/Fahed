% Creating the Geometry of the Problem
points = .95*[0 -2.5 0 -1; -2.2 0 0.1 0];
sp = spmak(-4:8,[points points]);
f = fnplt(sp,[0 4]);
pg2 = polyshape(f(1,:)',f(2,:)','Simplify',true);
tr = triangulation(pg2);
tnodes = tr.Points';
telements = tr.ConnectivityList';
plot(pg2)
%%
% Creating the Model for the PDE
model = createpde;
% Feeding it the triangular mesh
model.geometryFromMesh(tnodes, telements)
% Applying Dirichlet BC
% Dirichlet:
% hu=r
% Robin boundary condition 
% n·(c∇u)+qu=g
applyBoundaryCondition(model,'neumann','Edge',1,'g',1,'q',2);
applyBoundaryCondition(model,'dirichlet','Edge',1,'u', 0 );
generateMesh(model,"Hmax",0.05);
pdemesh(model)
%%
% Defining the Equation Symbolically [two-dimensional problem u(x,y)]
syms x
syms y
syms t
syms a(x,y,t)
syms b(x,y,t)
syms f(a,b)
syms g(a,b)
syms Da
syms Db
pdeeq[1] = -diff(u[1],t) + Da * laplacian(a,[x, y]) + f;
pdeeq[2] = -diff(u[2],t) + Db * laplacian(b, [x, y]) + g;
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
% define m and d
specifyCoefficients(model,'m',0,'d',1,'c',coeffs1.c,'a',coeffs1.a,'f',coeffs1.f);
results = solvepde(model);
u = results.NodalSolution;
msh = results.Mesh;

%%
figure
pdeplot(msh, XYData=u)

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