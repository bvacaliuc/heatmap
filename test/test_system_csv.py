#!/usr/bin/env python
"""Test case."""

from helper import TestHeatmap, unittest, ROOT_DIR

import os
import subprocess


class Tests(TestHeatmap):

    def test_system(self):
        output_file = os.path.join(ROOT_DIR, 'test', 'output.ppm')
        try:
            self.helper_run(
                [os.path.join(ROOT_DIR, 'heatmap.py'),
                 '-b', 'black',
                 '-r', '3',
                 '-W', '22',
                 '-P', 'equirectangular',
                 '-o', output_file,
                 '--ignore_csv_header',
                 os.path.join(ROOT_DIR, 'test', 'few-points.csv')])

            subprocess.check_call(
                ['perceptualdiff',
                 os.path.join(ROOT_DIR, 'test', 'few-points.ppm'),
                 output_file])
        finally:
            try:
                os.remove(output_file)
            except OSError:
                pass  # perhaps it was never created

    def test_weights(self):
        output_file = os.path.join(ROOT_DIR, 'test', 'output.png')
        try:
            self.helper_run(
                [os.path.join(ROOT_DIR, 'heatmap.py'),
                 '-W', '640',
                 '-d', '0.20',
                 '-o', output_file,
                 '--ignore_csv_header',
                 os.path.join(ROOT_DIR, 'test', 'weights.csv')])

            subprocess.check_call(
                ['perceptualdiff',
                 os.path.join(ROOT_DIR, 'test', 'weights.png'),
                 output_file])
        finally:
            try:
                os.remove(output_file)
            except OSError:
                pass  # perhaps it was never created

if __name__ == '__main__':
    unittest.main()
