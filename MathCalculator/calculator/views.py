# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .forms import MathForm
from .forms import DerivativeForm

from .equations import *
#from equations import testEquationCalculator
#from .equation-solver import testEquationCalculator

def index(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "index.html", {"form": form, "formattedEquation": formattedEquation})

def algebra(request):
	return render(request, "algebra.html")

def algebra_equations(request):
	return render(request, "equations.html")

def algebra_equations_system(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = solveSystemOfEquations(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "system.html", {"form": form, "formattedEquation": formattedEquation})

def algebra_equations_solve_equation(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = solveForVariable(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "solve-equation.html", {"form": form, "formattedEquation": formattedEquation})


def algebra_equations_expressions(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "expressions.html", {"form": form, "formattedEquation": formattedEquation})


def algebra_slope(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "slope.html", {"form": form, "formattedEquation": formattedEquation})

def algebra_graph(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "graph.html", {"form": form, "formattedEquation": formattedEquation})

def algebra_composition(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "composition.html", {"form": form, "formattedEquation": formattedEquation})

def algebra_partial_fractions(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "partial-fractions.html", {"form": form, "formattedEquation": formattedEquation})

def calculus(request):
	return render(request, "calculus.html")

def calculus_derivatives(request):
	return render(request, "derivatives.html")

def calculus_derivatives_standard(request):
	formattedEquation = ""
	if request.method == "POST":
		form = DerivativeForm(request.POST)
		if form.is_valid():
			formattedEquation = standardDerivative(form.cleaned_data["textarea"], form.cleaned_data["text"])
	else:
		form = DerivativeForm()
	return render(request, "derivatives-standard.html", {"form": form, "formattedEquation": formattedEquation})

def calculus_derivatives_partial(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "derivatives-partial.html", {"form": form, "formattedEquation": formattedEquation})


def calculus_integrals(request):
	return render(request, "integrals.html")

def calculus_integrals_indefinite(request):
	formattedEquation = ""
	if request.method == "POST":
		form = DerivativeForm(request.POST)
		if form.is_valid():
			formattedEquation = indefiniteIntegral(form.cleaned_data["textarea"], form.cleaned_data["text"])
	else:
		form = DerivativeForm()
	return render(request, "integrals-indefinite.html", {"form": form, "formattedEquation": formattedEquation})

def calculus_integrals_definite(request):
	formattedEquation = ""
	if request.method == "POST":
		form = DerivativeForm(request.POST)
		if form.is_valid():
			formattedEquation = definiteIntegral(form.cleaned_data["textarea"], form.cleaned_data["text"])
	else:
		form = DerivativeForm()
	return render(request, "integrals-definite.html", {"form": form, "formattedEquation": formattedEquation})

def calculus_graphical(request):
	return render(request, "graphical.html")

def calculus_graphical_arc_length(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "arc-length.html", {"form": form, "formattedEquation": formattedEquation})
    
def calculus_graphical_tangent_line(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "tangent-line.html", {"form": form, "formattedEquation": formattedEquation})

def calculus_graphical_critical_points(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "critical-points.html", {"form": form, "formattedEquation": formattedEquation})


def calculus_limits(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "limits.html", {"form": form, "formattedEquation": formattedEquation})

def ODE(request):
	return render(request, "ODE.html")

def ODE_first(request):
	formattedEquation = ""
	if request.method == "POST":
		form = DerivativeForm(request.POST)
		if form.is_valid():
			formattedEquation = ODESolver(form.cleaned_data["textarea"], form.cleaned_data["text"])
	else:
		form = DerivativeForm()
	return render(request, "ODE-first.html", {"form": form, "formattedEquation": formattedEquation})
    
def ODE_first_linear(request):
	formattedEquation = ""
	if request.method == "POST":
		form = DerivativeForm(request.POST)
		if form.is_valid():
			formattedEquation = ODESolver(form.cleaned_data["textarea"], form.cleaned_data["text"])
	else:
		form = DerivativeForm()
	return render(request, "ODE-first-linear.html", {"form": form, "formattedEquation": formattedEquation})
    
def ODE_first_separable(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "ODE-first-separable.html", {"form": form, "formattedEquation": formattedEquation})
    
def ODE_first_exact(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "ODE-first-exact.html", {"form": form, "formattedEquation": formattedEquation})
    
def ODE_first_euler(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "ODE-first-euler.html", {"form": form, "formattedEquation": formattedEquation})

def ODE_second(request):
	return render(request, "ODE-second.html")
    
def ODE_second_homogenous(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "ODE-second-homogenous.html", {"form": form, "formattedEquation": formattedEquation})
    
def linear_algebra(request):
	return render(request, "linear-algebra.html")

def linear_algebra_matrix_ops(request):
	return render(request, "matrix-ops.html")
    
def linear_algebra_matrix_ops_multiplication(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = matrix_multiplication(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "matrix-multiplication.html", {"form": form, "formattedEquation": formattedEquation})
    
def linear_algebra_matrix_ops_addition(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = matrix_addition(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "matrix-addition.html", {"form": form, "formattedEquation": formattedEquation})
    
def linear_algebra_matrix_ops_equation(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "matrix-equation.html", {"form": form, "formattedEquation": formattedEquation})
    
def linear_algebra_system(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "matrix-system.html", {"form": form, "formattedEquation": formattedEquation})

def linear_algebra_info(request):
	return render(request, "matrix-info.html")
    
def linear_algebra_info_RREF(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = matrix_RREF(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "matrix-RREF.html", {"form": form, "formattedEquation": formattedEquation})
    
def linear_algebra_info_determinant(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = matrix_determinant(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "matrix-determinant.html", {"form": form, "formattedEquation": formattedEquation})
    
def linear_algebra_info_transpose(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = matrix_transpose(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "matrix-transpose.html", {"form": form, "formattedEquation": formattedEquation})
    
def linear_algebra_info_inverse(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = matrix_inverse(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "matrix-inverse.html", {"form": form, "formattedEquation": formattedEquation})
    
def linear_algebra_info_eigenvalues(request):
	formattedEquation = ""
	if request.method == "POST":
		form = MathForm(request.POST)
		if form.is_valid():
			formattedEquation = matrix_eigenvalues(form.cleaned_data["textarea"])
	else:
		form = MathForm()
	return render(request, "matrix-eigenvalues.html", {"form": form, "formattedEquation": formattedEquation})
    
def geometry(request):
	return render(request, "geometry.html")

def geometry_area(request):
    formattedEquation = ""
    if request.method == "POST":
        form = MathForm(request.POST)
        if form.is_valid():
            formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
    else:
        form = MathForm()
    return render(request, "area.html", {"form": form, "formattedEquation": formattedEquation})

def geometry_Perimeter(request):
    formattedEquation = ""
    if request.method == "POST":
        form = MathForm(request.POST)
        if form.is_valid():
            formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
    else:
        form = MathForm()
    return render(request, "perimeter.html", {"form": form, "formattedEquation": formattedEquation})

def geometry_Triangles(request):
    return render(request, "Triangles.html", {"form": form, "formattedEquation": formattedEquation})

def geometry_Triangles_missingLen(request):
    formattedEquation = ""
    if request.method == "POST":
        form = MathForm(request.POST)
        if form.is_valid():
            formattedEquation = solveForVariable(form.cleaned_data["textarea"])
    else:
        form = MathForm()
    return render(request, "missingLen.html", {"form": form, "formattedEquation": formattedEquation})


def geometry_Triangles_missingAng(request):
    formattedEquation = ""
    if request.method == "POST":
        form = MathForm(request.POST)
        if form.is_valid():
            formattedEquation = solveForVariable(form.cleaned_data["textarea"])
    else:
        form = MathForm()
    return render(request, "missingAng.html", {"form": form, "formattedEquation": formattedEquation})

def geometry_Triangles_compareTri(request):
    formattedEquation =	""
    if request.method == "POST":
        form = MathForm(request.POST)
        if form.is_valid():
            pass
    else:
            form = MathForm()
    return render(request, "compareTri.html", {"form": form, "formattedEquation": formattedEquation})


def geometry_arclength_circle(request):
    formattedEquation = ""
    if request.method == "POST":
        form = MathForm(request.POST)
        if form.is_valid():
            formattedEquation = testEquationCalculator(form.cleaned_data["textarea"])
        else:
            form = MathForm()
        return render(request, "arclength-circle.html", {"form": form, "formattedEquation": formattedEquation})
