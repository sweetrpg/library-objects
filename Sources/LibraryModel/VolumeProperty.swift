//
// Volume.swift
// Copyright (c) 2021 Paul Schifferer.
//

import Fluent
import Vapor


public final class VolumeProperty : Model {
    public static let schema = VolumeProperty.v20210828.schemaName

    @ID
    public var id : UUID?

    @Timestamp(key: VolumeProperty.v20210828.createdAt, on: .create)
    public var createdAt : Date?

    @Timestamp(key: VolumeProperty.v20210828.updatedAt, on: .update)
    public var updatedAt : Date?

    @Field(key: VolumeProperty.v20210828.name)
    public var name : String

    @Field(key: VolumeProperty.v20210828.type)
    public var type : String

    @Field(key: VolumeProperty.v20210828.value)
    public var value : String

    @Parent(key: VolumeProperty.v20210828.volumeId)
    public var volume : Volume

    public init() {
    }

    public init(id : UUID? = nil, name : String, type : String, value : String, volumeId : Volume.IDValue) {
        self.id = id
        self.name = name
        self.type = type
        self.value = value
        self.$volume.id = volumeId
    }

}

extension VolumeProperty : Content {}
