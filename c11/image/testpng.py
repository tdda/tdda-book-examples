from PIL import Image
from tdda.referencetest import ReferenceTestCase, tag

class TestPNG(ReferenceTestCase):
    def testIdenticalPNGsDirectly(self):
        # Should pass: identical files
        self.assertBinaryFileCorrect('ref-graph.png', 'ref-graph-clone.png')

    def testDifferentPNGsWithSameImage(self):
        # Should fail: identical files
        self.assertBinaryFileCorrect('ref-graph.png',
                                     'same-pixels-as-ref-graph.png')

    def testBytesInDifferentPNGsWithSameImage(self):
        # Should pass: different files; same pixels
        ref = Image.open('ref-graph.png')
        actual = Image.open('same-pixels-as-ref-graph.png')
        self.assertEqual(ref.tobytes(), actual.tobytes())

if __name__ == '__main__':
    ReferenceTestCase.main()
