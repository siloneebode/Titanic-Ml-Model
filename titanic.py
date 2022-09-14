{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2c182bae",
   "metadata": {},
   "source": [
    "# IMPORTATIONN DES MODULES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "89135aba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting numpy\n",
      "  Downloading numpy-1.23.3-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.1 MB)\n",
      "\u001b[2K     \u001b[38;2;249;38;114m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[38;5;237m╺\u001b[0m\u001b[38;5;237m━\u001b[0m \u001b[32m16.3/17.1 MB\u001b[0m \u001b[31m345.4 kB/s\u001b[0m eta \u001b[36m0:00:03\u001b[0m:03\u001b[0m\n",
      "\u001b[?25h\u001b[31mERROR: Exception:\n",
      "Traceback (most recent call last):\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py\", line 435, in _error_catcher\n",
      "    yield\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py\", line 516, in read\n",
      "    data = self._fp.read(amt) if not fp_closed else b\"\"\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_vendor/cachecontrol/filewrapper.py\", line 90, in read\n",
      "    data = self.__fp.read(amt)\n",
      "  File \"/usr/lib/python3.9/http/client.py\", line 458, in read\n",
      "    n = self.readinto(b)\n",
      "  File \"/usr/lib/python3.9/http/client.py\", line 502, in readinto\n",
      "    n = self.fp.readinto(b)\n",
      "  File \"/usr/lib/python3.9/socket.py\", line 704, in readinto\n",
      "    return self._sock.recv_into(b)\n",
      "  File \"/usr/lib/python3.9/ssl.py\", line 1241, in recv_into\n",
      "    return self.read(nbytes, buffer)\n",
      "  File \"/usr/lib/python3.9/ssl.py\", line 1099, in read\n",
      "    return self._sslobj.read(len, buffer)\n",
      "socket.timeout: The read operation timed out\n",
      "\n",
      "During handling of the above exception, another exception occurred:\n",
      "\n",
      "Traceback (most recent call last):\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/cli/base_command.py\", line 167, in exc_logging_wrapper\n",
      "    status = run_func(*args)\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/cli/req_command.py\", line 247, in wrapper\n",
      "    return func(self, options, args)\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/commands/install.py\", line 369, in run\n",
      "    requirement_set = resolver.resolve(\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/resolver.py\", line 92, in resolve\n",
      "    result = self._result = resolver.resolve(\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py\", line 481, in resolve\n",
      "    state = resolution.resolve(requirements, max_rounds=max_rounds)\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py\", line 348, in resolve\n",
      "    self._add_to_criteria(self.state.criteria, r, parent=None)\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py\", line 172, in _add_to_criteria\n",
      "    if not criterion.candidates:\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_vendor/resolvelib/structs.py\", line 151, in __bool__\n",
      "    return bool(self._sequence)\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py\", line 155, in __bool__\n",
      "    return any(self)\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py\", line 143, in <genexpr>\n",
      "    return (c for c in iterator if id(c) not in self._incompatible_ids)\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py\", line 47, in _iter_built\n",
      "    candidate = func()\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/factory.py\", line 206, in _make_candidate_from_link\n",
      "    self._link_candidate_cache[link] = LinkCandidate(\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py\", line 297, in __init__\n",
      "    super().__init__(\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py\", line 162, in __init__\n",
      "    self.dist = self._prepare()\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py\", line 231, in _prepare\n",
      "    dist = self._prepare_distribution()\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py\", line 308, in _prepare_distribution\n",
      "    return preparer.prepare_linked_requirement(self._ireq, parallel_builds=True)\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/operations/prepare.py\", line 438, in prepare_linked_requirement\n",
      "    return self._prepare_linked_requirement(req, parallel_builds)\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/operations/prepare.py\", line 483, in _prepare_linked_requirement\n",
      "    local_file = unpack_url(\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/operations/prepare.py\", line 165, in unpack_url\n",
      "    file = get_http_url(\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/operations/prepare.py\", line 106, in get_http_url\n",
      "    from_path, content_type = download(link, temp_dir.path)\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/network/download.py\", line 147, in __call__\n",
      "    for chunk in chunks:\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/cli/progress_bars.py\", line 53, in _rich_progress_bar\n",
      "    for chunk in iterable:\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_internal/network/utils.py\", line 63, in response_chunks\n",
      "    for chunk in response.raw.stream(\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py\", line 573, in stream\n",
      "    data = self.read(amt=amt, decode_content=decode_content)\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py\", line 538, in read\n",
      "    raise IncompleteRead(self._fp_bytes_read, self.length_remaining)\n",
      "  File \"/usr/lib/python3.9/contextlib.py\", line 135, in __exit__\n",
      "    self.gen.throw(type, value, traceback)\n",
      "  File \"/home/silone/.local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py\", line 440, in _error_catcher\n",
      "    raise ReadTimeoutError(self._pool, None, \"Read timed out.\")\n",
      "pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.\u001b[0m\u001b[31m\n",
      "\u001b[0m"
     ]
    },
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'numpy'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn [3], line 4\u001b[0m\n\u001b[1;32m      1\u001b[0m get_ipython()\u001b[38;5;241m.\u001b[39msystem(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mpip install numpy\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m      3\u001b[0m \u001b[38;5;66;03m# numpy sert pour gérer les tableaux et matrices à n dimentions \u001b[39;00m\n\u001b[0;32m----> 4\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m \n\u001b[1;32m      6\u001b[0m \u001b[38;5;66;03m#os (operating system permet de charger les fichiers )\u001b[39;00m\n\u001b[1;32m      8\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mos\u001b[39;00m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'numpy'"
     ]
    }
   ],
   "source": [
    "!pip install numpy \n",
    "\n",
    "# numpy sert pour gérer les tableaux et matrices à n dimentions \n",
    "import numpy as np \n",
    "\n",
    "#os (operating system permet de charger les fichiers )\n",
    "\n",
    "import os "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03e413e6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
