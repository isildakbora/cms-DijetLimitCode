#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array


gROOT.SetBatch(kTRUE);
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetCanvasBorderMode(0)
gStyle.SetFrameBorderMode(0)
gStyle.SetCanvasColor(kWhite)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadRightMargin(0.05)
gStyle.SetPadTopMargin(0.05)
gStyle.SetPadBottomMargin(0.15)
gROOT.ForceStyle()


masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
xs_CSVL = array('d', [0.22014500000000001, 0.17674799999999999, 0.153363, 0.12456, 0.11397699999999999, 0.095328999999999997, 0.088451199999999994, 0.069897200000000007, 0.063809199999999996, 0.058266600000000002, 0.053023199999999999, 0.047611500000000001, 0.042187599999999999, 0.038328899999999999, 0.033851600000000003, 0.029336899999999999, 0.029057599999999999, 0.025583700000000001, 0.024107199999999999, 0.021452599999999999, 0.019949100000000001, 0.018297299999999999, 0.017465100000000001, 0.016785600000000001, 0.016048199999999999, 0.0144747, 0.0143334, 0.014110899999999999, 0.0137459, 0.013693200000000001, 0.0136291])
xs_CSVM = array('d', [0.1825, 0.151117, 0.15068999999999999, 0.121875, 0.10750999999999999, 0.097135700000000005, 0.097382999999999997, 0.084646700000000005, 0.086879799999999993, 0.084238499999999994, 0.077741299999999999, 0.068715899999999996, 0.061657400000000001, 0.059060799999999997, 0.055930899999999999, 0.051798900000000002, 0.048503299999999999, 0.046142500000000003, 0.044478999999999998, 0.040961900000000002, 0.039080700000000003, 0.0377001, 0.034931799999999999, 0.035287600000000002, 0.0344053, 0.035699500000000002, 0.036099899999999997, 0.038411599999999997, 0.041616199999999999, 0.042936299999999997, 0.046966899999999999])
xs_TCHEL = array('d', [0.47043499999999999, 0.35800199999999999, 0.29352400000000001, 0.233567, 0.193527, 0.15989400000000001, 0.14411399999999999, 0.12598100000000001, 0.095170400000000002, 0.082367599999999999, 0.074670100000000003, 0.054225200000000001, 0.048223299999999997, 0.041477, 0.034570299999999998, 0.032104500000000001, 0.0243962, 0.022158799999999999, 0.018633400000000001, 0.015673200000000002, 0.0137816, 0.011923700000000001, 0.0104025, 0.0090986000000000001, 0.0081037999999999995, 0.0072367300000000002, 0.0064590100000000003, 0.0059135200000000002, 0.00524042, 0.0045534800000000004, 0.0039711399999999997])

g_CSVL = TGraph(len(masses),masses,xs_CSVL)
g_CSVL.SetMarkerStyle(24)
g_CSVL.SetMarkerColor(kGreen+2)
g_CSVL.SetLineWidth(2)
g_CSVL.SetLineStyle(1)
g_CSVL.SetLineColor(kGreen+2)
g_CSVL.GetXaxis().SetTitle("Resonance Mass [GeV]")
g_CSVL.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
g_CSVL.GetYaxis().SetRangeUser(1e-03,10)
g_CSVL.GetXaxis().SetNdivisions(1005)

g_CSVM = TGraph(len(masses),masses,xs_CSVM)
g_CSVM.SetMarkerStyle(25)
g_CSVM.SetMarkerColor(kRed)
g_CSVM.SetLineWidth(2)
g_CSVM.SetLineStyle(2)
g_CSVM.SetLineColor(kRed)

g_TCHEL = TGraph(len(masses),masses,xs_TCHEL)
g_TCHEL.SetMarkerStyle(26)
g_TCHEL.SetMarkerColor(kBlue)
g_TCHEL.SetLineWidth(2)
g_TCHEL.SetLineStyle(3)
g_TCHEL.SetLineColor(kBlue)


c = TCanvas("c", "",800,800)
c.cd()

g_CSVL.Draw("AL")
g_CSVM.Draw("L")
g_TCHEL.Draw("L")

legend = TLegend(.45,.60,.85,.80)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader("Exp. 95% CL Upper Limits (stat. only)")
legend.AddEntry(g_TCHEL, "TCHEL","l")
legend.AddEntry(g_CSVL, "CSVL","l")
legend.AddEntry(g_CSVM, "CSVM","l")
legend.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.52, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.89, "qq/bb, f_{b#bar{b}}=1.0")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.43, "CMS Preliminary")
l1.DrawLatex(0.18,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.19,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.18,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.18,0.20, "Wide Jets")
l1.SetTextSize(0.055)
l1.DrawLatex(0.73,0.84, "2 b-tags")

c.SetLogy()
c.SaveAs('CSVL_CSVM_TCHEL_2Tag_limit_exp_SplusB_WideJets_Zprime_fbb1.0.eps')
