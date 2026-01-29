import datetime
import xlwings as xlw
from tdda.referencetest import ReferenceTestCase, tag

def copy_cells(source, dest, cols, rows, formula=False):
    for col in cols:
        for row in rows:
            ref = f'{col}{row}'
            if formula:
                dest[ref].formula = source[ref].formula
            else:
                dest[ref].value = source[ref].value

class TestExcel(ReferenceTestCase):
    @classmethod
    def setUpClass(cls):
        cls.was_open = len(xlw.apps) > 0  # Remember whether Excel was open

    @classmethod
    def tearDownClass(cls):
        if not cls.was_open:  # close if this code opened Excel
            xlw.apps.active.quit()

    def sales_test(self, proc_path, ref_path, test_path):
        try:
            # Open the three spreadsheets
            proc_wb = xlw.Book(proc_path)
            ref_wb = xlw.Book(ref_path)
            test_wb = xlw.Book(test_path)

            # Copy the reference inputs and outputs from the ref workbook
            # into the corresponding sheets in test workbook
            ref_inputs_sheet = ref_wb.sheets['Sales & Targets']
            out_inputs_sheet = test_wb.sheets['Sales & Targets']

            copy_cells(ref_inputs_sheet, out_inputs_sheet, 'BCDFGH',
                       range(3, 15))

            ref_results_sheet = ref_wb.sheets['Reference Results']
            out_ref_results_sheet = test_wb.sheets['Reference Results']

            copy_cells(ref_results_sheet, out_ref_results_sheet, 'BCD',
                             list(range(3, 15)) + [16])

            # Copy the FORMULAS for checking whether targets are met
            # from the analysis spreadsheet to the test spreadsheet
            proc_scores_sheet = proc_wb.sheets['Targets Met']
            out_scores_sheet = test_wb.sheets['Targets Met']
            copy_cells(proc_scores_sheet, out_scores_sheet, 'BCD',
                       range(3, 14), formula=True)
            test_wb.app.calculate()  # force recalculation just in case

            # Read the number of failures and pass rate from
            # the summary statistics on the last sheet in the test workbook.
            pass_fail_sheet = test_wb.sheets['PASS & FAIL STATS']
            failures = pass_fail_sheet['B4'].value
            pass_rate = pass_fail_sheet['B6'].value
            failed = failures > 0 or pass_rate < 1

            # If the test fails, write the failing spreadsheet and report
            if failed:
                date = datetime.datetime.now().isoformat(timespec='seconds')
                outpath = f'{date}-FAIL-{test_path}'.replace(':', '')
                test_wb.save(outpath)
                print(f'Written failing test workbook to {outpath}.')

            # Make the assertions.
            #  (Could just self.assertFalse(failed) instead)
            self.assertEqual(failures, 0)
            self.assertEqual(pass_rate, 1.0)
        finally:
            # Close the spreadsheets
            proc_wb.close()
            ref_wb.close()
            test_wb.close()

    def test_main_process_case_1(self):
        self.sales_test('sales-analysis-process.xlsx',
                        'test-case-1.xlsx', 'ref-test-1.xlsx')

    def test_main_process_case_2(self):
        self.sales_test('sales-analysis-process.xlsx',
                        'test-case-2.xlsx', 'ref-test-1.xlsx')

    def test_broken_process_case_1(self):
        # Should fail! Broken process.
        self.sales_test('broken-sales-analysis.xlsx',
                        'test-case-1.xlsx', 'ref-test-1.xlsx')

if __name__ == '__main__':
    ReferenceTestCase.main()
