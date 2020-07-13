# Lint as: python3

# Copyright 2020 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Command-line interface."""

import fire

from tfrutil import client
from tfrutil import check


def main():
  """Entry point for command-line interface."""

  fire.Fire({
      'create-tfrecords': client.create_tfrecords,
      'check-tfrecords': check.check_tfrecords,
  })


if __name__ == '__main__':
  main()