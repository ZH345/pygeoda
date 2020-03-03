import unittest
import pygeoda
__author__ = "Xun Li <lixun910@gmail.com>, "

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("./data/Guerry.shp")
        self.queen_w = pygeoda.weights.queen(self.guerry)
        select_vars = ["Crm_prs", "Crm_prp", "Litercy", "Donatns", "Infants", "Suicids"]
        self.data = [self.guerry.GetRealCol(v) for v in select_vars]
        self.Crm_prs = self.guerry.GetRealCol('Crm_prs')
        self.Crm_prp = self.guerry.GetRealCol('Crm_prp')
    def test_hinge15breaks(self):
        breaks = pygeoda.hinge15breaks(5,self.data)
        self.assertAlmostEqual(len(breaks),5)
    def test_pca(self):
        pca_r = pygeoda.pca(self.data)
        b1 = pca_r.getEigenValues()
        b2 = pca_r.getKaiser()
        b3 = pca_r.getMethod()
        b4 = pca_r.getPropOfVar()
        b5 = pca_r.getStandardDev()
        b6 = pca_r.getThresh95()
        b7 = pca_r.getLoadings()
        b8 = pca_r.getSqCorrelations()
        b9 = pca_r.getCumProp()


        self.assertAlmostEqual(b1,tuple((2973766400.0, 317174944.0, 63650252.0, 22336498.0, 5546270.0, 482.1877746582031)))
        self.assertAlmostEqual(b2,6.0)
        self.assertAlmostEqual(b3,'svd')
        self.assertAlmostEqual(b4,tuple((0.8791688084602356, 0.0937700867652893, 0.018817657604813576, 0.006603596732020378, 0.001639707712456584, 1.4255472535751323e-07)))
        self.assertAlmostEqual(b5,tuple((54532.25, 17809.40625, 7978.11083984375, 4726.150390625, 2355.052001953125, 21.95877456665039)))
        self.assertAlmostEqual(b6,1.0)
        self.assertAlmostEqual(b9,tuple((0.8791688084602356, 0.9729388952255249, 0.9917565584182739, 0.9983601570129395, 0.9999998807907104, 1.0)))
       
    def test_PCA(self):
        #data=[self.Crm_prs,self.Crm_prp]
        pca_r = pygeoda.pca(self.data)
        
        #self.assertEqual(pca_r.getCumProp(),tuple((0.8791688084602356, 0.9729388952255249, 0.9917565584182739, 0.9983601570129395, 0.9999998807907104, 1.0)))
        
        b1 = pca_r.getEigenValues()
        b2 = pca_r.getKaiser()
        b3 = pca_r.getMethod()
        b4 = pca_r.getPropOfVar()
        b5 = pca_r.getStandardDev()
        b6 = pca_r.getThresh95()
        b7 = pca_r.getLoadings()
        b8 = pca_r.getSqCorrelations()
        b9 = pca_r.getCumProp()
        pca_r.getStandardDev
        p=pygeoda.PCA(pca_r)
        a1 = p.getEigenValues()
        a2 = p.getKaiser()
        a3 = p.getMethod()
        a4 = p.getPropOfVar()
        a5 = p.getStandarDev()
        a6 = p.getThresh95()
        a7 = p.getLoadings()
        a8 = p.getSqCorrelations()
        a9 = p.getCumProp()
        self.assertAlmostEqual(a1,b1)
        self.assertAlmostEqual(a2,b2)
        self.assertAlmostEqual(a3,b3)
        self.assertAlmostEqual(a4,b4)
        self.assertAlmostEqual(a5,b5)
        self.assertAlmostEqual(a6,b6)
        self.assertAlmostEqual(a9,b9)
        #self.assertAlmostEqual(p.getmm(),tuple((0.8791688084602356, 0.9729388952255249, 0.9917565584182739, 0.9983601570129395, 0.9999998807907104, 1.0)))
        #方法svd
        #数据转换 raw
        #result = pygeoda.pca(self.data)

        """
        todo: convert the following c++ unit test to python unit test
              delete this section when finish
        EXPECT_STRCASEEQ(result->getMethod().c_str(), "svd");
        EXPECT_THAT(result->getStandardDev(),
                ElementsAre(1.46303403, 1.09581947, 1.04978454, 0.816680014, 0.740725815, 0.583970726));
        EXPECT_THAT(result->getPropOfVar(),
                    ElementsAre(0.356744826, 0.200136751, 0.183674619, 0.111161061, 0.0914457887, 0.0568369664));
        EXPECT_THAT(result->getCumProp(),
                    ElementsAre(0.356744826, 0.556881547, 0.74055618, 0.851717234, 0.943163037, 1.000000));
        EXPECT_FLOAT_EQ(result->getKaiser(), 3.0);
        EXPECT_FLOAT_EQ(result->getThresh95(), 5.0);
        EXPECT_THAT(result->getEigenValues(),
                    ElementsAre(2.1404686, 1.20082033, 1.10204756, 0.666966259, 0.548674762, 0.341021806));
        """