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
xs_CSVL = array('d', [0.211867, 0.17444499999999999, 0.13428799999999999, 0.11565599999999999, 0.099118700000000004, 0.076368500000000006, 0.0684757, 0.068145899999999995, 0.056385299999999999, 0.050083500000000003, 0.042538300000000001, 0.038610800000000001, 0.032862000000000002, 0.027311200000000001, 0.027270599999999999, 0.026530999999999999, 0.023123999999999999, 0.0154284, 0.0134725, 0.0102446, 0.0088475800000000007, 0.0074508999999999999, 0.0069642200000000001, 0.0060536799999999997, 0.0054501000000000003, 0.0049948299999999996, 0.0041914600000000002, 0.0038072399999999999, 0.0034146300000000001, 0.00302681, 0.0025611399999999999])
xs_CSVM = array('d', [0.164411, 0.139958, 0.122562, 0.099496399999999999, 0.083797300000000005, 0.070780800000000005, 0.059604699999999997, 0.052155899999999998, 0.044704399999999998, 0.045080799999999997, 0.042712600000000003, 0.0390176, 0.033817699999999999, 0.0281175, 0.0265045, 0.023905699999999998, 0.021625999999999999, 0.017090999999999999, 0.0125729, 0.0107102, 0.0088479300000000004, 0.0074508200000000004, 0.0065547599999999998, 0.0060536000000000001, 0.0052387099999999997, 0.0050058699999999999, 0.0041909499999999997, 0.0036661200000000001, 0.0032596299999999999, 0.0028115000000000002, 0.0023283100000000001])
xs_TCHEL = array('d', [0.42854399999999998, 0.32816400000000001, 0.23841899999999999, 0.20111200000000001, 0.161249, 0.13428699999999999, 0.110601, 0.094774999999999998, 0.075028600000000001, 0.0596053, 0.058742599999999999, 0.0553499, 0.044483799999999997, 0.033877200000000003, 0.028496299999999999, 0.0285784, 0.024027, 0.0184548, 0.014345500000000001, 0.0111764, 0.0097789000000000001, 0.0083818999999999994, 0.0069849200000000004, 0.0062009500000000002, 0.0055524900000000002, 0.0047083899999999998, 0.0041578199999999996, 0.0034924600000000002, 0.0030268399999999998, 0.0027939699999999998, 0.0023508600000000002])

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
l1.DrawLatex(0.18,0.89, "Z'-like, f_{b#bar{b}}=1.0")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.43, "CMS Preliminary")
l1.DrawLatex(0.18,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.19,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.18,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.18,0.20, "Wide Jets")
l1.SetTextSize(0.055)
l1.DrawLatex(0.535,0.84, "0, 1 and 2 b-tags")

c.SetLogy()
c.SaveAs('CSVL_CSVM_TCHEL_Combined_limit_exp_WideJets_Zprime_fbb1.0.eps')
