# Copyright (c) 2024 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The `Tensor` template `tensor.prototype.pyi` for `tools/gen_tensor_stub.py` to generate the stub file `tensor.pyi`.
# Add docstring, attributes, methods and alias with type annotaions for `Tensor` in `tensor.prototype.pyi`
# if not conveniently coding in original place (like c++ source file).

# Import common typings for generated methods
# isort: off
from typing import *  # noqa: F403
from typing_extensions import *  # type: ignore # noqa: F403
from paddle._typing import *  # noqa: F403

# isort: on

from typing import Any, Iterator, Literal, Protocol, overload

import numpy.typing as npt

import paddle
from paddle import (
    ParamAttr,  # noqa: F401
    _typing,
)
from paddle.base.dygraph.tensor_patch_methods import (
    TensorHookRemoveHelper,  # noqa: F401
)

# annotation: ${eager_param_base_begin}
class AbstractEagerParamBase(Protocol):
    # annotation: ${eager_param_base_docstring}

    # annotation: ${eager_param_base_attributes}

    # annotation: ${eager_param_base_methods}
    @property
    def trainable(self) -> bool: ...
    @trainable.setter
    def trainable(self, trainable: bool) -> None: ...

    # annotation: ${eager_param_base_alias}

# annotation: ${eager_param_base_end}

# annotation: ${tensor_begin}
class AbstractTensor(Protocol):
    # annotation: ${tensor_docstring}

    # annotation: ${tensor_attributes}

    # If method defined below, we should make the method's signature complete,
    # and ignore the signature extracted from `paddle.Tensor`.
    # `gen_tensor.stub.py` will NOT overwrite the signature below.
    # If method has docstring (ignoring the spaces), `gen_tensor.stub.py` also will NOT overwrite it.

    # annotation: ${tensor_methods}
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, dtype, dims, name: str, type, persistable: bool
    ) -> None: ...
    @overload
    def __init__(
        self,
        value: npt.NDArray[Any],
        place,
        persistable: bool,
        zero_copy: bool,
        name: str,
        stop_gradient: bool,
    ) -> None: ...
    @overload
    def __init__(self, value: npt.NDArray[Any]) -> None: ...
    @overload
    def __init__(self, value: Tensor) -> None: ...
    @overload
    def __init__(
        self, value: Tensor, place, name: str, process_mesh, placements
    ) -> None: ...
    @overload
    def __init__(
        self, value: Tensor, dims, name: str, process_mesh, placements
    ) -> None: ...
    @overload
    def __init__(self, value: Tensor, place, name: str) -> None: ...
    @overload
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        ref: paddle/fluid/pybind/eager.cc

        We should have init function with signature:
        1.
        def __init__ ()
        2.
        def __init__ (
            dtype: paddle::framework::proto::VarType::Type,
            dims: vector<int>,
            name: std::string,
            type: paddle::framework::proto::VarType::LodTensor,
            persistable: bool)
        3. (multi-place)
        (should have at least one parameter, one parameter equals to case 4, zero
        parameter equals to case 1)
        def __init__ (
            value: ndarray,
            place: paddle::platform::Place,
            persistable: bool,
            zero_copy: bool,
            name: std::string,
            stop_gradient: bool)
        4.
        def __init__ (
            value: ndarray)
        5.
        def __init__ (
            tensor: Tensor)
        6. (multi-place)
        (should have at least one parameter, one parameter equals to case 5, zero
        parameter equals to case 1.)
        def __init__ (
            global_tensor: Tensor,
            place: paddle::platform::Place,
            name: std::string,
            process_mesh: phi::distributed::ProcessMesh
            placements: std::vector<Placement>)
        7. (multi-place)
        (should have at least one parameter, one parameter equals to case 5, zero
        parameter equals to case 1.)
        def __init__ (
            local_tensor: Tensor,
            global_dims: vector<int>,
            name: std::string,
            process_mesh: phi::distributed::ProcessMesh
            placements: std::vector<Placement>)
        8. (multi-place) (should have at least one parameter, one parameter similar
        to case 5, zero parameter equals to case 1.)
        def __init__ (
            tensor: FrameworkTensor,
            place: paddle::platform::Place,
            name: std::string)
        """
        ...
    # rich comparison
    def __eq__(self, y: _typing.TensorLike) -> Tensor: ...  # type: ignore[override]
    def __ge__(self, y: _typing.TensorLike) -> Tensor: ...
    def __gt__(self, y: _typing.TensorLike) -> Tensor: ...
    def __lt__(self, y: _typing.TensorLike) -> Tensor: ...
    def __le__(self, y: _typing.TensorLike) -> Tensor: ...
    def __ne__(self, y: _typing.TensorLike) -> Tensor: ...  # type: ignore[override]

    # binary arithmetic operations
    def __add__(self, y: _typing.TensorLike) -> Tensor: ...
    def __sub__(self, y: _typing.TensorLike) -> Tensor: ...
    def __mul__(self, y: _typing.TensorLike) -> Tensor: ...
    def __matmul__(self, y: _typing.TensorLike) -> Tensor: ...
    def __truediv__(self, y: _typing.TensorLike) -> Tensor: ...
    def __floordiv__(self, y: _typing.TensorLike) -> Tensor: ...
    def __mod__(self, y: _typing.TensorLike) -> Tensor: ...
    def __pow__(self, y: _typing.TensorLike) -> Tensor: ...
    def __and__(self, y: _typing.TensorLike) -> Tensor: ...
    def __div__(self, y: _typing.TensorLike) -> Tensor: ...
    def __radd__(self, y: _typing.TensorLike) -> Tensor: ...  # type: ignore
    def __rsub__(self, y: _typing.TensorLike) -> Tensor: ...  # type: ignore
    def __rmul__(self, y: _typing.TensorLike) -> Tensor: ...  # type: ignore
    def __rtruediv__(self, y: _typing.TensorLike) -> Tensor: ...  # type: ignore
    def __rpow__(self, y: _typing.TensorLike) -> Tensor: ...  # type: ignore
    def __rdiv__(self, y: _typing.TensorLike) -> Tensor: ...

    # type cast
    def __bool__(self) -> bool: ...
    def __float__(self) -> float: ...
    def __int__(self) -> int: ...
    def __long__(self) -> float: ...
    def __nonzero__(self) -> bool: ...

    # emulating container types
    def __getitem__(
        self,
        item: _typing.TensorIndex,
    ) -> Tensor: ...
    def __setitem__(
        self,
        item: _typing.TensorIndex,
        value: Tensor | npt.NDArray[Any] | complex | bool,
    ) -> None: ...
    def __len__(self) -> int: ...

    # emulating numeric types
    def __index__(self) -> int: ...

    # unary arithmetic operations
    def __invert__(self) -> Tensor: ...
    def __neg__(self) -> Tensor: ...

    # basic
    def __hash__(self) -> int: ...
    def clear_gradient(self, set_to_zero: bool = True) -> None: ...
    def clone(self) -> Tensor: ...
    def cols(self) -> Tensor: ...
    def contiguous(self) -> Tensor: ...
    def copy_(self) -> Tensor: ...
    def crows(self) -> Tensor: ...
    @property
    def data(self) -> Tensor: ...
    @data.setter
    def data(self, value: Tensor) -> None: ...
    def data_ptr(self) -> int: ...
    def detach(self) -> Tensor: ...
    def detach_(self) -> Tensor: ...
    @property
    def dtype(self) -> paddle.dtype: ...
    def element_size(self) -> int: ...
    def get_map_tensor(self) -> Tensor: ...
    def get_selected_rows(self) -> None: ...
    def get_strides(self) -> list[int]: ...
    def get_tensor(self) -> Tensor: ...
    @property
    def grad(self) -> Tensor | None: ...
    @grad.setter
    def grad(self, value: Tensor) -> None: ...
    @property
    def grad_(self) -> Tensor | None: ...
    @grad_.setter
    def grad_(self, value: Tensor) -> None: ...
    @property
    def grad_fn(self) -> Any: ...
    def is_contiguous(self) -> bool: ...
    def is_dense(self) -> bool: ...
    def is_dist(self) -> bool: ...
    @property
    def is_leaf(self) -> bool: ...
    def is_same_shape(self, y: Tensor) -> bool: ...
    def is_selected_rows(self) -> bool: ...
    def is_sparse(self) -> bool: ...
    def is_sparse_coo(self) -> bool: ...
    def is_sparse_csr(self) -> bool: ...
    @property
    def layout(self) -> _typing.DataLayoutND: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def ndim(self) -> int: ...
    def nnz(self) -> int: ...
    @property
    def num_shard(self) -> int: ...
    def numpy(self) -> npt.NDArray[Any]: ...
    @property
    def offset(self) -> int: ...
    @property
    def persistable(self) -> bool: ...
    @persistable.setter
    def persistable(self, value: bool) -> None: ...
    @property
    def place(self) -> paddle.core.Place: ...
    @property
    def placements(self) -> list[paddle.distributed.Placement] | None: ...
    @property
    def process_mesh(self) -> paddle.distributed.ProcessMesh | None: ...
    def rows(self) -> list[int]: ...
    def set_string_list(self, value: str) -> None: ...
    def set_vocab(self, value: dict) -> None: ...
    @property
    def shape(self) -> list[int]: ...
    @property
    def size(self) -> int: ...
    @property
    def stop_gradient(self) -> bool: ...
    @stop_gradient.setter
    def stop_gradient(self, value: bool) -> None: ...
    @property
    def strides(self) -> list[int]: ...
    @property
    def type(self) -> Any: ...

    # virtual methods
    def __iter__(self) -> Iterator[Tensor]: ...  # For iterating over the tensor

    # private methods
    def _grad_ivar(self) -> Tensor | None: ...

    # annotation: ${tensor_alias}
    __qualname__: Literal["Tensor"]

# annotation: ${tensor_end}

class Tensor(AbstractTensor, AbstractEagerParamBase): ...
